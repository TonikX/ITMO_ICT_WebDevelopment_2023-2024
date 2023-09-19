import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))
sock.send(b"GET /scores?subject=test HTTP/1.1\nContent-Type: text")
print(sock.recv(1024 * 4).decode())
