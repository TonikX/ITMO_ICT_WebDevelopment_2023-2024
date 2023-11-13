import socket


class AbstractServer:
    _address_and_port: tuple = ("127.0.0.1", 8080)
    _timeout: float = 0.5
    _protocol = socket.SOCK_DGRAM
    _server_socket: socket.socket = None

    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, self._protocol)
        self._server_socket.bind(self._address_and_port)
        self._server_socket.settimeout(self._timeout)
        print("...Server is running...")

    def _exit(self) -> None:
        print("Server is shutting down...")
        self._server_socket.close()

    def _action(self):
        pass

    def cycle(self) -> None:
        try:

            while True:
                try:
                    self._action()

                except socket.timeout:
                    pass

        except KeyboardInterrupt:
            pass

        finally:
            self._exit()
