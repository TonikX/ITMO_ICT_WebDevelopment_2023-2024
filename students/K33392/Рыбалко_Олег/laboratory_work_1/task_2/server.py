import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(1)

conn, addr = sock.accept()
print("Received new connection from", addr)

conn.send(b"Enter a and b splitted by the space, for example: 10 20")

data = conn.recv(1024)
a, b = list(map(int, data.decode().split()))
result = (a**2 + b**2)**0.5
conn.sendall(str(result).encode())
conn.close()