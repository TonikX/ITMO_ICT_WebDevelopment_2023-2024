from socket import *

ip = '127.0.0.1'
port = 3000

server = socket(AF_INET, SOCK_DGRAM)
server.bind((ip, port))

while True:
    msg, addr = server.recvfrom(1024)
    print(msg.decode("utf-8"))
    server.sendto(b"Hello, client", addr)