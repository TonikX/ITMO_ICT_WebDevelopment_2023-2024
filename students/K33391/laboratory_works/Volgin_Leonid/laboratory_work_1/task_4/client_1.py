import socket
import threading
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 2002))

def send():
    while True:
        try:
            data = input()
            if data == 'exit':
                break
            client.send(data.encode('utf-8'))
        except:
            print('disconnection')
            break
    client.close()

def listen():
    while True:
        try:
            indata = client.recv(1024)
            print(indata.decode('utf-8'))
        except:
            print('disconnection')
            break
t1 = threading.Thread(target=listen)
t2 = threading.Thread(target=send)

t1.start()
t2.start()