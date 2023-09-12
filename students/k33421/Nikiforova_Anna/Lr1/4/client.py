import socket
import threading
from config import HOST, SERVER_PORT, BUFF_SIZE


class Client:
    def __init__(self, server_address):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conn.connect(server_address)
            name_question = self.conn.recv(BUFF_SIZE).decode("utf-8")
            name = input(name_question)
            self.name = name
            self.conn.sendall(name.encode('utf-8'))
            print(f"Вы присоединились к чату как {self.name}")

            threading.Thread(target=self.send_messages, args=()).start()
            threading.Thread(target=self.recieve_messages(), args=()).start()
        except ConnectionRefusedError:
            print("Сервер недоступен, попробуйте позже")

    def send_messages(self):
        while True:
            try:
                message = input()
                self.conn.sendall(message.encode("utf-8"))
            except (OSError, EOFError):
                break

    def recieve_messages(self):
        while True:
            try:
                message = self.conn.recv(BUFF_SIZE)
                if not message:
                    break
                print(message.decode("utf-8"))
            except (OSError, EOFError):
                break


if __name__ == "__main__":
    server_address = (HOST, SERVER_PORT)
    client = Client(server_address)
