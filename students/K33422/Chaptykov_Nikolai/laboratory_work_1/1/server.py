import socket
import sys

HOST = 'localhost'
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

while True:

    data, addr = s.recvfrom(1024)
    print('Received: ' + data.decode('utf-8'))

    message = 'Hello, client!'
    s.sendto(message.encode('utf-8'), addr)