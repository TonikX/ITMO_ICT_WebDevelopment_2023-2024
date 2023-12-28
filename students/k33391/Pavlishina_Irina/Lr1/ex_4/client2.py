import socket
import threading
import random

PORT = 8080


def listen_chat(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)


def write_chat(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


def main():

    global PORT

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))
    message = client_socket.recv(4096)
    print(message.decode())
    nick = input()
    client_socket.send(nick.encode('utf-8'))
    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()


if __name__ == "__main__":
    main()