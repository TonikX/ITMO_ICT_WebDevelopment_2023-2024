from base_classes.AbstractServer import AbstractServer
import socket
class Server3(AbstractServer):

    _protocol = socket.SOCK_STREAM
    _connections_number = 5

    def __init__(self):
        super().__init__()
        self._server_socket.listen(self._connections_number)

    def _action(self) -> None:
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


if __name__ == "__main__":
    server = Server3()
    server.cycle()

