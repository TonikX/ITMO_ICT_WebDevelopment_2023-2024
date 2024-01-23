import socket
import threading


def send_message():
    while True:
        msg = input()
        socket.send(msg.encode())


def receive_message():
    while True:
        msg = socket.recv(128).decode()
        if not msg:
            break
        print(msg)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 55555))

send_thread = threading.Thread(target=send_message)
send_thread.start()
recv_thread = threading.Thread(target=receive_message)
recv_thread.start()
