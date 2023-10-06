### Задание 4: 
Здесь задача была создать много пользовательский чат. Для этого определяем модуль сервера и нескольких клиентов.

#### Реализация части логики клиентской части+ выбор мода:

from students.K33392.laboratory_works.Пронина_Александра.laboratory_work_1.task_4.server import ChatServer

import socket
import threading


class ChatClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 456
        self.client_socket = None

    def start(self):
        nickname = input("Enter your nickname: ")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.sendall(nickname.encode())

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.client_socket.sendall(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
                else:
                    break
            except:
                break


if __name__ == "__main__":
    mode = input("Choose mode (server/client): ")

    if mode == "server":
        server = ChatServer()
        server.start()
    elif mode == "client":
        client = ChatClient()
        client.start()
    else:
        print("Invalid mode")

#### Реализация логики серверной части

import socket
import threading


class ChatServer:
    def __init__(self):
        self.host = 'localhost'
        self.port = 456
        self.server_socket = None
        self.clients = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        print("Chat server started on {}:{}".format(self.host, self.port))

        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        nickname = client_socket.recv(1024).decode()
        print("{} connected".format(nickname))

        self.broadcast("{} joined the chat".format(nickname))

        self.clients.append((nickname, client_socket))

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.broadcast("{}: {}".format(nickname, message))
                else:
                    self.remove_client(nickname, client_socket)
                    break
            except():
                self.remove_client(nickname, client_socket)
                break

    def remove_client(self, nickname, client_socket):
        client_socket.close()
        self.clients.remove((nickname, client_socket))
        self.broadcast("{} left the chat".format(nickname))

    def broadcast(self, message):
        for client in self.clients:
            client[1].sendall(message.encode())
