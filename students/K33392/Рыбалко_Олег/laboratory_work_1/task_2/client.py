import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 9090)

sock.connect(addr)

hello_msg = sock.recv(1024).decode()
print(hello_msg)

data = input().encode()
sock.send(data)
print(sock.recv(1024).decode())
