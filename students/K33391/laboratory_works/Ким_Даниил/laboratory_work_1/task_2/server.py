import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.bind(("localhost", 9099))
conn.listen(1)

clientsocket, addr = conn.accept()
print("Received new connection from", addr)

clientsocket.send(b"Enter two numbers to get hypotenuse, for example: 23 34")

data = clientsocket.recv(1024)

a, b = list(map(int, data.decode().split()))

clientsocket.send(str((a**2 + b**2)**0.5).encode())

# close connection
conn.close()