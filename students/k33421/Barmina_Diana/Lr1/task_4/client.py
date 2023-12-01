import socket
from threading import Thread


def get_messages():
    while True:
        get = conn.recv(16384).decode("utf-8")
        print(get)


def post_messages():
    while True:
        post = input()
        conn.sendall(post.encode('utf-8'))


if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 14900))
    name = input("Ваше имя: \n")
    receive_th = Thread(target=get_messages)
    receive_th.start()
    respond_th = Thread(target=post_messages)
    respond_th.start()
