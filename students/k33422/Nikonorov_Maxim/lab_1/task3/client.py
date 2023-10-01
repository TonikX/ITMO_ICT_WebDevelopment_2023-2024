import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 49001)) 

req = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"

sock.send(req.encode("utf-8"))
data = sock.recv(1024).decode("utf-8")

print(data)

sock.close()
