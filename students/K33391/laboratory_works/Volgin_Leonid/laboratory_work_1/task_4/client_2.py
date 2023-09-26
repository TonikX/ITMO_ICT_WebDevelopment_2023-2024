import socket
import threading
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 2002))


def send():
    while True:
        data = input()
        client.send(data.encode('utf-8'))

def listen():
    while True:
        indata = client.recv(1024)
        print(indata.decode('utf-8'))

t1 = threading.Thread(target=listen)
t2 = threading.Thread(target=send)

t1.start()
t2.start()