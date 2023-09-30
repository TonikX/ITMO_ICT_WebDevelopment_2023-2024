import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 9090))
data, address = sock.recvfrom(1024)

print(data.decode("utf-8"))
sock.sendto(b"Hello, client", address)

sock.close()
