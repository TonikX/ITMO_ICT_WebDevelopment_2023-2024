import socket
import threading
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 2002))

def send():
    while True:
        msg = input()
        client.send(bytes(msg, "UTF-8"))
def listen():
    while True:
        time.sleep(1)
        data = client.recv(4096)
        print(data.decode("UTF-8"))
#client.send(bytes('web', "UTF-8"))
time.sleep(1)
#mouth = threading.Thread(target=send)
ear = threading.Thread(target=listen)
#mouth.start()
#ear.start()
while True:

    data = client.recv(4096)
    print(data.decode("UTF-8"))
#data = client.recv(4096)
#print(data)
client.close()