import math
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
                try:
                    self._wait_for_signal()
                except socket.timeout:
                    pass
        finally:
            self.exit_gracefully()

    def _wait_for_signal(self) -> None:
        client_socket, address = self._server_socket.accept()
        print(f"Connection from {address} has been established!")
        client_socket.send("Введите через запятую без пробелов значения a и b".encode())
        data = client_socket.recv(self._buffer_size).decode()
        a, b = (int(num) for num in data.split(","))
        gcd = math.gcd(a, b)
        client_socket.send(f"GCD: {gcd}".encode())
        print(f"Connection from {address} has been closed!")

    def exit_gracefully(self) -> None:
        print("Server is shutting down...")
        self._server_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    server = Server()
    server.start_cycle()
