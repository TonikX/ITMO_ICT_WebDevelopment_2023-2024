from socket import *

ip= '127.0.0.1'
port = 3000

client = socket(AF_INET, SOCK_DGRAM)
client.connect((ip, port))
client.send(b"Hello, server")
server_message = client.recvfrom(1024)
msg = server_message[0].decode()
print(msg)