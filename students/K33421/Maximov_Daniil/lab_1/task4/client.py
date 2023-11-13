import socket
import sys
import threading


class Client:
    _address_and_port: tuple = ("127.0.0.1", 8080)

    _client_socket: socket.socket = None

    _server_closed: bool = False

    _timeout: int = 1

    _name: str

    # init ------------------------------------------------------------------

    def __init__(self) -> None:
        print("введите имя пользователя")
        try:
            name = input()
            self._name = name

        except:
            sys.exit(0)

    # Connecting and reciving ------------------------------------------------------------------
    def connect_to_chat(self) -> None:
        self._setup_client_socket()
        self._start_listening_for_input_in_background()

        print("...Client is running...")

        try:
            while True:
                if self._server_closed:
                    break

                self._try_getting_message_from_server()

        except KeyboardInterrupt:
            pass

        finally:
            self._exit()

    def _try_getting_message_from_server(self) -> None:
        try:
            message = self._client_socket.recv(1024)

            if not message:
                print("Сервер закрыл соединение!")
                self._server_closed = True

            print(message.decode())

        except socket.timeout:
            pass

    # Exiting ------------------------------------------------------------------
    def _setup_client_socket(self) -> None:
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client_socket.connect(self._address_and_port)
        self._client_socket.settimeout(self._timeout)

    def _exit(self) -> None:
        self._server_closed = True
        print("Exiting chat...")
        self._client_socket.close()
        sys.exit(0)

    # Listening ------------------------------------------------------------------
    def _start_listening_for_input_in_background(self) -> None:
        thread = threading.Thread(target=self._listen_for_input)
        thread.daemon = True
        thread.start()

    def _listen_for_input(self) -> None:
        try:
            while True:
                user_input = input()
                self._send_message_to_chat(f'<{self._name}> : {user_input}')

        except:
            pass

    # Send_message ------------------------------------------------------------------
    def _send_message_to_chat(self, message: str) -> None:
        self._client_socket.sendall(message.encode())


if __name__ == "__main__":
    client = Client()
    client.connect_to_chat()
