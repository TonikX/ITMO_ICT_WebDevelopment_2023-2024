import socket

message = input()

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(message.encode('utf-8'))

data = s.recv(1024)
print(data.decode('utf-8'))

data = s.recv(1024)
print(data.decode('utf-8'))

s.close()