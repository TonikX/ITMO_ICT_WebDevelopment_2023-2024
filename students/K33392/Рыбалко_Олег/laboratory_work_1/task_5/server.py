import json
import logging
import socket
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

logging.basicConfig(level=logging.INFO)
SCORES = defaultdict(list)


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class HTTPRequest:
    method: HTTPMethod
    protocol: str
    path: str
    headers: dict[str, str]
    body: bytes


@dataclass
class HTTPResponse:
    status: int
    headers: dict[str, str]
    body: bytes
    protocol: str = "HTTP/1.1"

    def __bytes__(self):
        headers_str = "\n".join(f"{key}: {val}" for key, val in self.headers.items())
        return f"{self.protocol} {self.status} {HTTPStatus(self.status).phrase}\n{headers_str}\n\n".encode() + self.body


class HTTPServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.__socket = None

    def serve(self):
        if self.__socket is None:
            raise ValueError("socket is None")

        self.__socket.bind((self.host, self.port))
        self.__socket.listen(1)
        logging.info(f"Started server on {self.host}:{self.port}")

        while True:
            conn, addr = self.__socket.accept()
            try:
                self.__handle_client(conn)
            except Exception as e:
                logging.error(f"failed to serve client {addr}: {e}")

    def __enter__(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def __exit__(self, *_):
        logging.info("Shutting down the server")
        self.__socket.close()

    def __handle_client(self, conn: socket.socket):
        req = self.__parse_request(conn)
        resp = self.__handle_request(req)
        self.__send_response(conn, resp)

    def __send_response(self, conn: socket.socket, resp: HTTPResponse):
        logging.info(f"Sent {conn.send(bytes(resp))} bytes")

    def __handle_request(self, req: HTTPRequest):
        logging.info(f"Got {req.method} request {req.path}")
        if req.method == HTTPMethod.GET and req.path.startswith("/scores"):
            query_params = parse_qs(urlparse(req.path).query)
            if "subject" not in query_params:
                return HTTPResponse(
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"detail": "subject query param was not specified"}).encode(),
                )
            return HTTPResponse(
                status=200,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"score": SCORES[query_params["subject"][0]]}).encode(),
            )
        elif req.method == HTTPMethod.POST and req.path.startswith("/subject"):
            query_params = parse_qs(urlparse(req.path).query)
            if "name" not in query_params:
                return HTTPResponse(
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"detail": "name query param was not specified"}).encode(),
                )
            if "score" not in query_params:
                return HTTPResponse(
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"detail": "score query param was not specified"}).encode(),
                )
            SCORES[query_params["name"][0]].append(query_params["score"][0])
            return HTTPResponse(status=200, headers={}, body=b"")
        return HTTPResponse(status=404, headers={}, body=b"")

    def __parse_request(self, conn: socket.socket) -> HTTPRequest:
        f = conn.recv(1024 * 6)
        lines = f.splitlines()

        # Parse start-line
        try:
            method, path, protocol = lines[0].decode().strip().split()
        except IndexError:
            raise Exception("Malformed start-line")

        # Parse headers
        headers: dict[str, str] = {}
        index = 1
        req_generator = ((n, i.decode()) for n, i in enumerate(lines[1:], 1))
        while (data := next(req_generator, None)) is not None and data[1].strip() != "":
            index, header = data
            try:
                key, val = header.split(":")
                headers[key.lower()] = val.strip()
            except ValueError:
                raise Exception("Malformed headers")

        # Parse body
        body = b"".join(lines[index + 2 :])
        return HTTPRequest(HTTPMethod(method), protocol, path, headers, body)


if __name__ == "__main__":
    with HTTPServer("localhost", 9090) as server:
        server.serve()
