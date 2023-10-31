import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

message = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
sock.send(message.encode())

data = sock.recv(BUFFER_SIZE)
print(data.decode())

sock.close()