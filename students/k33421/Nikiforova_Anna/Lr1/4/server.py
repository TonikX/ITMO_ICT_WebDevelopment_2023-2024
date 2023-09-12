import socket
import threading
from config import HOST, SERVER_PORT, BUFF_SIZE


class Server:
    def __init__(self, server_address):
        self.clients = {}  # {socket: name}

        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind(server_address)
        self.conn.listen(10)
        print('Server is listening...')

    def get_messages(self, client_socket):
        while True:
            try:
                message = client_socket.recv(BUFF_SIZE).decode()
                print(f"Recieved message '{message}' from {self.clients[client_socket]}")
                if message:
                    self.broadcast(client_socket, message)
            except (ConnectionResetError, OSError):
                name = self.clients[client_socket]
                print(f"{name} disconnected from chat")
                self.broadcast(client_socket, f"{name} вышел из чата!", add_name=False)
                del self.clients[client_socket]
                break

    def broadcast(self, client_socket, message, add_name=True):
        name = self.clients[client_socket]
        for client in self.clients:
            if client != client_socket:
                if add_name:
                    client.sendall(f"{name}: {message}".encode())
                else:
                    client.sendall(message.encode())

    def run(self):
        try:
            while True:
                client_socket, addr = self.conn.accept()

                client_socket.sendall("Введите ваше имя на сервере: ".encode('utf-8'))
                name = client_socket.recv(BUFF_SIZE).decode('utf-8')
                self.clients[client_socket] = name
                print(f"{name} added to chat")
                self.broadcast(client_socket, f"{name} присоединился к чату!", add_name=False)

                threading.Thread(target=self.get_messages, args=(client_socket,)).start()
        except KeyboardInterrupt:
            self.broadcast("", f"Чат завершен!", add_name=False)
            self.clients = {}
            self.conn.close()
            print(f"Server stopped")


if __name__ == "__main__":
    server_address = (HOST, SERVER_PORT)
    server = Server(server_address)
    server.run()
