import socket
import sys

with open('index.html', 'r') as f:
	file = f.read()
print(file)

HOST = 'localhost'
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

s.listen(10)
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024)
    conn.close()