from base_classes.AbstractServer import AbstractServer


class Server1(AbstractServer):
    def __init__(self) -> None:
        super().__init__()

    def _action(self) -> None:
        data, address = self._server_socket.recvfrom(1024)
        print(f"Message: {data.decode()}")
        self._server_socket.sendto("Hello, client".encode(), address)


if __name__ == "__main__":
    server = Server1()
    server.cycle()
