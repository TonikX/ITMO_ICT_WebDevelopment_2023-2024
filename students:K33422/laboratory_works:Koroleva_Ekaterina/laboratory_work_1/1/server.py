from socket import *

# Настраиваем хост
host = 'localhost'
port = 10000
host_data = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(host_data)

conn, addr = udp_socket.recvfrom(1024)
print(conn.decode())
udp_socket.sendto(b"Hello, client!", addr)

