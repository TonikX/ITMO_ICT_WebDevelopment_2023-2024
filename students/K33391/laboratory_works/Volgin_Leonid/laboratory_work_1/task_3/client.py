import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost', 2001))
data = client.recv(32768)
print(data.decode('UTF-8'))
client.close()