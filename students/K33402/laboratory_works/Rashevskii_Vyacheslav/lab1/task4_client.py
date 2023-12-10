import socket
from threading import *


def receive():
    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)


def respond():
    while True:
        client.send((input()).encode('utf-8'))


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9090))

    nick = input('Enter your name: ')

    receive_th = Thread(target=receive)
    receive_th.start()

    client.send(nick.encode('utf-8'))
    respond()
