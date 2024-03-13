import socket

host = 'localhost'
port = 5555

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
sock.bind((host, port))

# Receive the message from the client
message, addr = sock.recvfrom(1024)
print(message.decode())

# Send a response message to the client
response_message = "Hello, client!"
sock.sendto(response_message.encode(), addr)