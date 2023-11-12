import socket
import sys


class Client:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size = 1024

    _client_socket: socket.socket = None

    def __init__(self) -> None:
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Client is running...")

    def send_message(self, message: str) -> None:
        self._client_socket.sendto(message.encode(), (self._address, self._port))
        data, _ = self._client_socket.recvfrom(self._buffer_size)
        print(f"Message: {data.decode()}")

    def exit_gracefully(self) -> None:
        print("Client is shutting down...")
        self._client_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    client = Client()

    try:
        client.send_message("Hello, server")
    finally:
        client.exit_gracefully()
