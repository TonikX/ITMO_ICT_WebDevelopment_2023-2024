import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(("127.0.0.1", 5000))
conn.send(b"Hello, server")
data, addr = conn.recvfrom(1024)
print(data.decode("utf-8"))
