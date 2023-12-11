import socket

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
s.sendall(request.encode())

data = s.recv(1024)
print(data.decode('utf-8'))

s.close()