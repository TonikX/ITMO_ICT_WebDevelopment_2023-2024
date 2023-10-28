import socket
import sys


class Server:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size: int = 1024

    _server_socket: socket.socket = None

    _timeout: int = 1

    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._server_socket.bind((self._address, self._port))
        self._server_socket.settimeout(self._timeout)
        print("Server is running...")

    def start_cycle(self) -> None:
        try:
            while True:
                try:
                    self._wait_for_signal()
                except socket.timeout:
                    pass
        finally:
            self.exit_gracefully()

    def _wait_for_signal(self) -> None:
        data, address = self._server_socket.recvfrom(self._buffer_size)
        print(f"Message: {data.decode()}")
        self._server_socket.sendto("Hello, client".encode(), address)

    def exit_gracefully(self) -> None:
        print("Server is shutting down...")
        self._server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    server = Server()
    server.start_cycle()
