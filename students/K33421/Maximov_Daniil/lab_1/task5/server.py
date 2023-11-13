import socket
import json
import sys
from collections import defaultdict
from typing import Any, Dict


class MyHTTPServer:
    _timeout: int = 1

    _server_socket: socket.socket = None

    _max_connections: int = 10

    _data: defaultdict[str, list[str]]

    _server_host: str

    _server_port: int

    _line_break: str = "\r\n"

    # init ------------------------------------------------------------------

    def __init__(self, host: str, port: int) -> None:
        self._data = defaultdict(list)
        self._server_host = host
        self._server_port = port
        self._serve_forever()
        print("...Server is running...")

    # setup ------------------------------------------------------------------
    def _serve_forever(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._server_host, self._server_port))
        self._server_socket.listen(self._max_connections)
        self._server_socket.settimeout(self._timeout)

    # serve ------------------------------------------------------------------
    def serve(self) -> None:
        try:
            while True:
                try:
                    socket_connection, _ = self._server_socket.accept()
                    socket_connection.settimeout(self._timeout)

                    try:
                        self._serve_client(socket_connection)

                    finally:
                        socket_connection.close()

                except (socket.timeout, socket.error):
                    pass

        finally:
            self._exit()

    # client ------------------------------------------------------------------
    def _serve_client(self, conn: socket.socket) -> None:
        request = conn.recv(1024).decode()

        if not request:
            return

        method, path, _ = self._parse_request(request)

        if path != "/":
            html_file = self._load_html_file("not_found.html")
            self._send_response(conn, html_file, status_code="404 Not Found")

        elif method == "GET":
            self._handle_get_request(conn)

        elif method == "POST":
            body = self._parse_body(request)
            self._handle_post_request(body, conn)

    # handle ------------------------------------------------------------------
    def _handle_get_request(self, conn: socket.socket) -> None:
        data_pairs = [f"{discipline}: {', '.join(grades)}" for discipline, grades in self._data.items()]
        formatted_scores = "<br>".join(data_pairs)
        placeholder = "###PLACEHOLDER###"
        html_file = self._load_html_file("index.html")
        processed_html_file = html_file.replace(placeholder, formatted_scores)
        self._send_response(conn, processed_html_file)

    def _handle_post_request(self, body: dict, conn: socket.socket) -> None:
        discipline = body.get("discipline", "")
        grade = body.get("grade", "")
        self._data[discipline].append(grade)
        self._send_response(conn)

    # parse  ------------------------------------------------------------------

    @staticmethod
    def _parse_body(request: str) -> dict[Any, Any] | Any:
        lines = request.split("\r\n")
        i = lines.index("")

        if len(lines) > i + 1:
            body = "\r\n".join(lines[i + 1:])
            return json.loads(body)

        return {}

    @staticmethod
    def _parse_request(request: str) -> tuple[str, str, str]:
        lines = request.split("\r\n")
        method, path, version = lines[0].split(" ")
        return method, path, version

    # load ------------------------------------------------------------------
    @staticmethod
    def _load_html_file(file_name: str) -> str:
        with open(file_name, encoding="utf-8") as f:
            html_file = f.read()

        return html_file

    def _serializer_headers(self, headers: dict[str, str]) -> str:
        pairs = [f"{name}: {value}{self._line_break}" for name, value in headers.items()]
        return "".join(pairs)

    def _send_response(self, conn: socket.socket, response: str = "", status_code: str = "200 OK") -> None:
        response_headers = {
            "Content-Type": "text/html; charset=utf-8",
            "Connection": "close",
        }
        response_headers_raw = self._serializer_headers(response_headers)
        protocol_version = "HTTP/1.1"
        header = f"{protocol_version} {status_code}"
        raw_response = header + self._line_break + response_headers_raw + self._line_break + response
        conn.sendall(raw_response.encode("utf-8"))

    # exit ------------------------------------------------------------------
    def _exit(self) -> None:
        print("..Server is shutting down...")
        self._server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    serv = MyHTTPServer(host, port)
    serv.serve()
