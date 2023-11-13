import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9090))
s.listen(1)
conn, addr = s.accept()
conn.sendall('Type in trapezoid bases and height'.encode())
data = conn.recv(1024).decode()
try:
    a_base, b_base, height = [float(x) for x in data.split()]
    area = (a_base + b_base) / 2 * height
    area = round(area, 3)
    conn.sendall(struct.pack('f', area))
except:
    conn.sendall('Data should be floats'.encode())

conn.close()


