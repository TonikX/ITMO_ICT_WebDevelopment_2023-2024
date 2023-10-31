
import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def receive_messages(sock):
    while True:
        data = sock.recv(BUFFER_SIZE)
        if not data:
            break
        message = data.decode()
        print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

name = input("Enter your name: ")
message = "Hello! My name is " + name
sock.send(message.encode())

receive_thread = threading.Thread(target=receive_messages, args=(sock,))
receive_thread.start()

while True:
    inp = input()
    message = name + ": " + inp
    if inp == 'exit':
        break
    sock.send(message.encode())

sock.close()