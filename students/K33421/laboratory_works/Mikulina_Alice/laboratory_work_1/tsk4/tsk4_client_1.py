import socket
import threading

server_address = input("Enter server address: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_address, 12345))

client_name = input("Enter your name: ")

client_socket.send(client_name.encode())

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def send():
    while True:
        message = input()
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()