import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(bytes("Hello, Server", "UTF-8"),('localhost', 2000))

data = client.recv(4096)
print(data.decode("UTF-8"))

client.close()