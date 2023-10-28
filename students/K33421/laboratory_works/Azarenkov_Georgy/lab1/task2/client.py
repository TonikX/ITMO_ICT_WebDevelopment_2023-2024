import socket
import sys


class Client:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size = 1024

    _client_socket: socket.socket = None

    def __init__(self) -> None:
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._open_connection()
        print("Client is running...")

    def calculate_gcd(self) -> None:
        question = self._receive_new_message()
        print("question", question)
        gcd_input_raw = input()
        self._send_message(gcd_input_raw)
        gcd = self._receive_new_message()
        print(gcd)

    def exit_gracefully(self) -> None:
        print("Client is shutting down...")
        self._client_socket.close()
        sys.exit(0)

    def _receive_new_message(self) -> str:
        return self._client_socket.recv(self._buffer_size).decode()

    def _send_message(self, message: str) -> None:
        self._client_socket.send(message.encode())

    def _open_connection(self) -> None:
        self._client_socket.connect((self._address, self._port))


if __name__ == "__main__":
    client = Client()

    try:
        client.calculate_gcd()

    finally:
        client.exit_gracefully()
