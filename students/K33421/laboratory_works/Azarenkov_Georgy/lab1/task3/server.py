import socket
import sys


class Server:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size: int = 1024

    _server_socket: socket.socket = None

    _timeout: int = 1

    _number_of_concurrent_connections: int = 10

    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._address, self._port))
        self._server_socket.settimeout(self._timeout)
        self._server_socket.listen(self._number_of_concurrent_connections)
        print("Server is running...")

    def start_cycle(self) -> None:
        try:
            while True:
                self._try_handling_message()
        finally:
            self.exit_gracefully()

    def _try_handling_message(self) -> None:
        try:
            client_socket, address = self._server_socket.accept()

            with open("index.html", encoding="utf-8") as f:
                index_html = f.read().encode()

            content_length = len(index_html)

            headers = (
                "HTTP/1.1 200 OK\n"
                "Content-Type: text/html\n"
                f"Content-Length: {content_length}\n"
                "Connection: close\n\n"
            ).encode()

            response = headers + index_html

            client_socket.sendall(response)

        except socket.timeout:
            pass

    def exit_gracefully(self) -> None:
        print("Server is shutting down...")
        self._server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    server = Server()
    server.start_cycle()
