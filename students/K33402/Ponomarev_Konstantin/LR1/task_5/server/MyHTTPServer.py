import json
import socket

from task_5.model.Method import Method
from task_5.model.Request import Request
from task_5.model.Response import Response
from urllib.parse import parse_qs, urlparse


class MyHTTPServer:
    _socket: socket.socket
    _grades: dict[str, int] = dict()

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def init(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen(1)
        print(f"server started in {self._host}:{self._port}")
        while True:
            client = self._socket.accept()
            try:
                response = self.handle_client_request(client[0])
                self.send_response(response, client[0])
            except Exception as error:
                print(f"{error}")

    def handle_client_request(self, client: socket.socket) -> Response:
        request = self.map_to_request_model(client)
        return self.get_response(request)

    def map_to_request_model(self, client: socket.socket) -> Request:
        data = client.recv(2048).splitlines()
        method, path, protocol_ver = data[0].decode().strip().split()
        headers, last_header_index = self.parse_headers(data[1:])
        body = b"".join(data[last_header_index + 2:])

        return Request(Method(method), path, protocol_ver, headers, body)

    def get_response(self, request) -> Response:
        print(f"get_response:{request.method} {request.path}")
        if request.method == Method.GET and request.path.startswith("/grades"):
            query_parameters = parse_qs(urlparse(request.path).query)
            if "subject" not in query_parameters:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "subject query param was not specified"}).encode(),
                )

            return Response(
                protocolVersion="HTTP/1.1",
                status=200,
                headers={"Content-Type": "text/html", "charset": "UTF-8"},
                body=self.generate_html().encode(),
            )
        elif request.method == Method.POST and request.path.startswith("/subject"):
            query_params = parse_qs(urlparse(request.path).query)
            if "name" not in query_params:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "name query param was not specified"}).encode(),
                )
            if "grade" not in query_params:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "score query param was not specified"}).encode(),
                )
            self._grades[query_params["name"][0]] = query_params["grade"][0]
            return Response(protocolVersion="HTTP/1.1", status=200, headers={}, body=b"")
        else:
            Response(protocolVersion="HTTP/1.1", status=404, headers={}, body=b"")

    def send_response(self, response: Response, client: socket.socket):
        client.send(response.to_byte())

    def parse_headers(self, data: list[bytes]) -> tuple[dict[str, str], int]:
        index = -1
        headers: dict[str, str] = dict()
        generator = ((n, i.decode()) for n, i in enumerate(data))
        while (line_data := next(generator, None)) is not None and line_data[1].strip() != "":
            index, header = line_data
            try:
                key, value = header.split(":")
                headers[key.lower()] = value.strip()
            except ValueError:
                raise Exception("Wrong header")

        return headers, index

    def generate_html(self):
        return (
            "<html><body>"
            f"{''.join([f'<div>{subject}: {grade}</div>' for subject, grade in self._grades.items()])}"
            "</body></html>"
        )
