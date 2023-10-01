import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9090))
print(s.recv(1024).decode())
data = input()
s.sendall(data.encode())

result = s.recv(1024)
s.close()
print('Trapezoid area is', *struct.unpack('f', result))
