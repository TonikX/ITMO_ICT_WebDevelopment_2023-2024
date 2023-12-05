import socket

server_ip = 'localhost'
server_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = 'Hello, server!'

sock.sendto(message.encode(), (server_ip, server_port))

data, server_address = sock.recvfrom(4096)
response = data.decode()

print('Server response:', response)

sock.close()