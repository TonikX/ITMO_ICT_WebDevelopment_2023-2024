import socket

host = 'localhost'
port = 9090
addr = (host,port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'Hello, server'
data = str.encode(data)
s.sendto(data, addr)

data = bytes.decode(data)
data = s.recvfrom(1024)
print(data)