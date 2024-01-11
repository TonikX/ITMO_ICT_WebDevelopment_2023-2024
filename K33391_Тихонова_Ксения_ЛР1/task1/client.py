import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_adress = ('localhost', 7777)
conn.connect(server_adress)

conn.send(b"Hello, server")

data = conn.recv(1024)
print(data.decode("utf-8"))

conn.close()