import socket
import threading


def get_messages():
    while True:
        message = server.recv(1024)
        if message:
            print(message.decode('utf-8'))


def send_messages():
    while True:
        server.send(input().encode('utf-8'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("localhost", 9097))

get_mess_thread = threading.Thread(target=get_messages)
get_mess_thread.start()

server.send(input("Enter your name: ").encode('utf-8'))

send_messages()