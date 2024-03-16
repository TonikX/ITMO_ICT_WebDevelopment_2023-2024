import socket

enc = "utf-8"
port = 2448
buffsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", port))

data = bytes("Hello, server", enc)
s.send(data)
print("Sent data to server:", data.decode(enc))

data = s.recv(buffsize)
print("Received data from server:", data.decode(enc))