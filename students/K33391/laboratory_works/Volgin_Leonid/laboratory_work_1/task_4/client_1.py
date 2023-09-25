import socket
import threading


def listen():
    while True:
        data = client.recv(4096)
        print(data.decode("UTF-8"))
def send():
    while True:
        message = input()
        client.send(bytes(message, "UTF-8"))


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 2002))


ear = threading.Thread(target=listen)
mouth = threading.Thread(target=send)
try:
    #ear.start()
    #mouth.start()
    while True:
        message = input()
        if message == "exit":
            break
        client.send(bytes(message, "UTF-8"))

except:
    print("smth went wrong")
client.close()