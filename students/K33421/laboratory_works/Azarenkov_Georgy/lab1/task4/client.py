import socket
import sys
import threading


class Client:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size = 1024

    _client_socket: socket.socket = None

    _timeout: int = 1

    _server_closed: bool = False

    def connect_to_chat(self) -> None:
        self._setup_client_socket()
        self._start_listening_for_input_in_background()

        print("Client is running...")

        try:
            while True:
                if self._server_closed:
                    break

                self._try_getting_message_from_server()

        except KeyboardInterrupt:
            pass

        finally:
            self._exit_gracefully()

    def _try_getting_message_from_server(self) -> str:
        try:
            message = self._client_socket.recv(self._buffer_size)

            if not message:
                print("Сервер закрыл соединение!")
                self._server_closed = True

            print(message.decode())

        except socket.timeout:
            pass

    def _setup_client_socket(self) -> None:
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client_socket.connect((self._address, self._port))
        self._client_socket.settimeout(self._timeout)

    def _exit_gracefully(self) -> None:
        self._server_closed = True
        print("Exiting chat...")
        self._client_socket.close()
        sys.exit(0)

    def _start_listening_for_input_in_background(self) -> None:
        thread = threading.Thread(target=self._listen_for_input)
        thread.daemon = True
        thread.start()

    def _listen_for_input(self) -> None:
        try:
            while True:
                user_input = input()
                self._send_message_to_chat(user_input)

        except:
            pass

    def _send_message_to_chat(self, message: str) -> None:
        self._client_socket.sendall(message.encode())


if __name__ == "__main__":
    client = Client()
    client.connect_to_chat()
