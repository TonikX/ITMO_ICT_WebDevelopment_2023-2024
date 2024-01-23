import socket


def receive_message():
    message = socket.recv(1024).decode()
    print(message)


server_address = ('localhost', 55555)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server_address)

receive_message()

socket.close()
