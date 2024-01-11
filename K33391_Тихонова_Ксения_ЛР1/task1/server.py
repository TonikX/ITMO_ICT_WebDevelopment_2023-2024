import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_adress = ('localhost', 7777)

conn.bind(server_adress)
data, address = conn.recvfrom(1024)

print(data.decode("utf-8"))
conn.sendto(b"Hello, client", address)

conn.close()