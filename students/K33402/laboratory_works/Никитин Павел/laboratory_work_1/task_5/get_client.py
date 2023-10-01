import socket

BUFFER = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))

request = "GET /scores?subject=test HTTP/1.1\nContent-Type: text"
sock.send(request.encode())

response = sock.recv(BUFFER).decode()
print(response)