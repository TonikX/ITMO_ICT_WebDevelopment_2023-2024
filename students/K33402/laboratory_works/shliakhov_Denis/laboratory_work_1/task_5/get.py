import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

request = "GET /marks?subject=math HTTP/1.1\nContent-Type: text"

sock.send(request.encode())

response = sock.recv(1024).decode()
print(response)
