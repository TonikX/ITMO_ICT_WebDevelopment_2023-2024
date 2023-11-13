import socket

from base_classes.AbstractServer import AbstractServer


class Server2(AbstractServer):
    _protocol = socket.SOCK_STREAM
    _connections_number = 5

    def __init__(self):
        super().__init__()
        self._server_socket.listen(self._connections_number)

    def _action(self):
        # вар d - поиск площади параллелограмма по стороне и высоте
        data, address = self._server_socket.accept()

        print(f" {address} - соединение установлено!")

        data.send("Введите через пробел сторону a высоту h".encode())

        users_answer = data.recv(1024).decode()

        a, h = (int(num) for num in users_answer.split())

        area = a * h

        if h > a:
            data.send("Высота не может быть больше стороны - введите еще раз".encode())
            self.cycle()

        print(f" ответ {area} отправлен пользователю")

        data.send(f" S = {area}".encode())

        print(f" {address} соединение разоравано")


if __name__ == "__main__":
    server = Server2()
    server.cycle()
