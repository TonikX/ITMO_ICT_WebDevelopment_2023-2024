from typing import List, Union, Tuple, Callable, Dict
from urllib.parse import parse_qs, urlparse
from email.parser import Parser
from loguru import logger
import socket
import json
import io

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048
MAX_PENDING_CONNECTIONS = 10

grades: Dict[str, List[int]] = {}


class Request:
    def __init__(
        self,
        method: str,
        target: str,
        version: str,
        headers,
        reader: io.BufferedReader,
    ):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.reader = reader
        self.__url = urlparse(self.target)
        self.path = self.__url.path
        self.query = parse_qs(self.__url.query)
        content_size = self.headers.get("Content-Length")
        self.body = (
            self.reader.read(int(content_size)) if content_size != None else None
        )


class Response:
    def __init__(
        self,
        status: int,
        reason: str,
        headers: Union[List[Tuple[str, Union[str, int]]], None] = None,
        body: Union[bytes, None] = None,
    ):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


RouteHandler = Callable[[Request], Response]


class MyHTTPServer:
    MAX_LINE_LEN = 64 * 1024
    MAX_HEADERS_COUNT = 100

    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__headers_parser = Parser()
        self.__rout_handlers: List[Tuple[str, str, RouteHandler]] = []

    def start(self):
        logger.info("Starting server...")
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            socket_conn.bind((self.__host, self.__port))
            socket_conn.listen(MAX_PENDING_CONNECTIONS)
            logger.info(f"Server started successfully on {self.__host}:{self.__port}")

            while True:
                try:
                    (client, _) = socket_conn.accept()
                    self.__serve_client(client)
                except KeyboardInterrupt:
                    break
        finally:
            socket_conn.close()
            logger.info("Server stopped, bye...")

    # @TODO: добавить парсинг generic паравметров внутри path
    # Привер: /get/<id>
    # Лучше всего реализовать через дерево поиска
    def add_route(self, path: str, method: str, handler: RouteHandler):
        self.__rout_handlers.append((path, method, handler))

    def __serve_client(self, client: socket.socket):
        try:
            request = self.__parse_request(client)
            logger.info(
                f"Proccess user request: {request.version} {request.method} {request.target}"
            )
            response = self.__handle_reqeust(request)
            logger.info(f"Return response: {response.status} {response.reason}")
            self.__send_response(client, response)

            request.reader.close()
            client.close()
        except HTTPError as error:
            self.__send_error(client, error)
        except Exception as e:
            logger.info(e)
            self.__send_error(client, HTTPError(500, "Internal Server Error"))

    def __parse_request(self, client: socket.socket):
        reqReader = client.makefile("rb")
        method, target, version = self.__parse_request_line(reqReader)
        headers = self.__parse_request_headers(reqReader)

        host = headers.get("Host")
        if not host:
            raise HTTPError(400, "Bad request", "Host header is missing")

        return Request(method, target, version, headers, reqReader)

    def __parse_request_line(self, reqReader: io.BufferedReader):
        raw_line = reqReader.readline(self.MAX_LINE_LEN + 1)
        if len(raw_line) > self.MAX_LINE_LEN:
            raise HTTPError(400, "Bad request", "Request line is too long")

        req_line = str(raw_line, "iso-8859-1")
        parts = req_line.split()
        if len(parts) != 3:
            raise HTTPError(400, "Bad request", "Malformed request line")

        method, target, version = parts
        if version != "HTTP/1.1":
            raise HTTPError(505, "HTTP Version Not Supported")

        return method, target, version

    def __parse_request_headers(self, reqReader: io.BufferedReader):
        headers = []
        while True:
            line = reqReader.readline(self.MAX_LINE_LEN + 1)
            if len(line) > self.MAX_LINE_LEN:
                raise HTTPError(494, "Request header too large")

            if line in (b"\r\n", b"\n", b""):
                break

            headers.append(line)
            if len(headers) > self.MAX_HEADERS_COUNT:
                raise HTTPError(494, "Too many headers")

        sheaders = b"".join(headers).decode("iso-8859-1")
        return self.__headers_parser.parsestr(sheaders)

    def __handle_reqeust(self, request: Request):
        for route in self.__rout_handlers:
            if request.path == route[0] and request.method == route[1]:
                return route[2](request)

        raise HTTPError(404, "Not Found")

    def __send_response(self, client: socket.socket, response: Response):
        resWriter = client.makefile("wb")
        status_line = f"HTTP/1.1 {response.status} {response.reason}\r\n"
        resWriter.write(status_line.encode("iso-8859-1"))

        if response.headers:
            for key, value in response.headers:
                header_line = f"{key}: {value}\r\n"
                resWriter.write(header_line.encode("iso-8859-1"))
        resWriter.write(b"\r\n")

        if response.body:
            resWriter.write(response.body)

        resWriter.flush()
        resWriter.close()

    def __send_error(self, client: socket.socket, err: HTTPError):
        status = err.status
        reason = err.reason
        body = (err.body or err.reason).encode("utf-8")

        response = Response(status, reason, [("Content-Length", len(body))], body)
        self.__send_response(client, response)
        logger.info(f"Return response: {response.status} {response.reason}")


def get_html_base(content: str):
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Grades</title>
        <style>
            table {{
                border-collapse: collapse;
                border-spacing: 0px;
            }}

            th,
            td {{
                padding: 5px;
                border: 1px solid black;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """


def grades_to_html_table():
    table_header = """
    <thead>
        <tr>
          <th>Subject</th>
          <th>Grades</th>
        </tr>
      </thead>
    """

    table_rows = []
    for subject in grades:
        table_rows.append(
            f"""
            <tr>
                <td>{subject}</td>
                <td>{', '.join(list(map(str, grades[subject])))}</td>
            </tr>
            """
        )

    table_rows = "\n".join(table_rows)
    table_body = f"<tbody>{table_rows}</tbody>"
    return get_html_base(f"<table>{table_header}\n{table_body}</table>")


def handle_get_grades(_: Request):
    body = grades_to_html_table()
    body = body.encode("utf-8")

    headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", len(body)),
    ]
    return Response(200, "OK", headers, body)


def handle_add_grade(req: Request):
    if req.headers["Content-Type"] != "application/json":
        raise HTTPError(400, "Bad request", "Wrong body Content-Type")

    body = json.loads(req.body or b"")
    if not "subject" in body or not "grade" in body or int(body.get("grade", 0)) < 0:
        raise HTTPError(400, "Bad request", "Wrong body params")

    if not body["subject"] in grades:
        grades[body["subject"]] = []
    grades[body["subject"]].append(body["grade"])

    response_body = json.dumps({"ok": True}).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", len(response_body)),
    ]
    return Response(200, "OK", headers, response_body)


if __name__ == "__main__":
    server = MyHTTPServer(HOST, PORT)

    server.add_route("/grades", "GET", handle_get_grades)
    server.add_route("/grades", "POST", handle_add_grade)

    server.start()
