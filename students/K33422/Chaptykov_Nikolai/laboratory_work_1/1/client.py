import socket

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

message = 'Hello server!'
s.sendto(message.encode('utf-8'), (HOST, PORT))

data = s.recv(1024)
print('Received: ' + data.decode('utf-8'))

s.close()