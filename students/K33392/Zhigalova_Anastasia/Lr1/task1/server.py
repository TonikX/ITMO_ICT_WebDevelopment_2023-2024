import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)

while True:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    s.sendto(b'Hello, Client!', addr)
