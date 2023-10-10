import socket
from time import sleep

serverIP = "192.168.56.1"
PORT = 14900
buffSize = 16384

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connection.connect((serverIP, PORT))

ms = "Hello, Server"
connection.sendto(ms.encode('utf-8'), (serverIP, PORT) )
#print(1)

data = (connection.recv(buffSize)).decode("utf-8")
print(data)
#print(2)