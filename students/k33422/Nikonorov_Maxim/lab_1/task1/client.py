import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 49001)
message = b"Hello, server!"

sock.sendto(message, server_address)

data, server = sock.recvfrom(1024)
print(data.decode("utf-8"))

sock.close()