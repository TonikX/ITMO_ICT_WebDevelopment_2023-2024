import socket

host = 'localhost'
port = 5555

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = "Hello, server!"
sock.sendto(message.encode(), (host, port))

# Receive a response from the server
response, _ = sock.recvfrom(1024)
print(response.decode())