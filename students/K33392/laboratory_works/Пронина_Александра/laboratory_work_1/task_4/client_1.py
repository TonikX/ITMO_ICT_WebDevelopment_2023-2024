
import socket
import threading

from students.K33392.laboratory_works.Пронина_Александра.laboratory_work_1.task_4.server import ChatServer


class ChatClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 4567
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
