import socket

serverIP = "192.168.56.1"
PORT = 14900
buffSize = 16384

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((serverIP, PORT))

 
try:
    data = connection.recv(buffSize)
    data = data.decode("utf-8")
    print(data)
 
finally:
    connection.close()