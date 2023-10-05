import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(addr)

message = s.recv(1024)
print(message.decode('utf-8'))

data = input().encode('utf-8')
s.send(data)
print(s.recv(1024).decode('utf-8'))