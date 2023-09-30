import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 9090))
sock.send(b"Hello, server")

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()
