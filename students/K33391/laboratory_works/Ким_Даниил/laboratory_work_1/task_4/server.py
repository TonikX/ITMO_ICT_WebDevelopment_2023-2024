import socket
import threading


class User:
    def __init__(self, conn):
        self.Conn = conn
        self.Name = ""


def send_everyone(message: str):
    for user in users:
        if user.Name != "":
            user.Conn.send(message.encode())


def chat(user: User):
    while True:
        try:
            data = user.Conn.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                raise

            data = data.decode('utf-8')
            if user.Name == "":
                user.Name = data
                send_everyone(f"{user.Name} joined the chat")
                continue

            send_everyone(user.Name + ": " + data)

        except (Exception,):
            users.remove(user)
            user.Conn.close()
            send_everyone(f"{user.Name} left the chat")
            break


def start():
    while True:
        conn, address = server.accept()
        user = User(conn)
        users.append(user)
        chat_thread = threading.Thread(target=chat, args=[user])
        chat_thread.start()


users = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9090))
server.listen()

start()
