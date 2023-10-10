import socket
from time import sleep

serverIP = "192.168.56.1"
PORT = 14900
buffSize = 16384

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((serverIP, PORT))

while True:
    ms = input()
    connection.send(ms.encode('utf8'))
    data = connection.recv(buffSize)
    print(data.decode("utf-8") + '\n')

#connection.close()