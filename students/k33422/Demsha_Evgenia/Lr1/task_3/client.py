import socket

host = "localhost"
port = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
result = client.recv(10000)
print(result.decode())
client.close()
