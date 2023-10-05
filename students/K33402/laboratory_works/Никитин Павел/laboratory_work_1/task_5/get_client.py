import socket

BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))

sock.send(b"GET / HTTP/1.1\r\nHost:localhost:8080\r\n\r\n")
response = sock.recv(BUFFER)

sock.close()
print(response.decode())