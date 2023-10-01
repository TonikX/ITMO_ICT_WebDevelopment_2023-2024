import socket
import threading


class ChatServer:
    _socket: socket
    _connections: list[socket.socket]

    def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(("localhost", 9090))
        print("server started")
        self._socket.listen(4)
        self.handle_connections(self._socket)

    def handle_client_message(self, connection: socket.socket, user_address: tuple):
        message = connection.recv(1024)
        try:
            while message is not None and message != b"Quit":
                self.send_message_to_clients(message, user_address)
        finally:
            connection.close()

    def send_message_to_clients(self, message: bytes, address: tuple):

        message = (f"{address[0]}:".encode("utf-8") + message + b"\n")

        # Нужно отправить всем подключением сообщение, исключая пользователя
        unreceived_users = set()
        for i, (connection, connectionAddress) in enumerate(self._connections):
            if address != connectionAddress:
                try:
                    connection.send(message)
                except OSError:
                    unreceived_users.add(i)

        unreceived_users = list(unreceived_users)
        for i in unreceived_users:
            self._connections.pop(i)

    def handle_connections(self, sock: socket.socket):
        print("server handle connections")
        while True:
            connection, address = sock.accept()
            print(f"Client connected: {address}")

            connection.send("Say hello to new user!")

            self.send_message_to_clients(f"New user has joined: {address}".encode(), ("Server", ""))

            self._connections.append((connection, address))

            client_thread = threading.Thread(
                target=self.handle_client_message,
                args=(
                    connection,
                    address,
                ),
            )
            client_thread.start()
