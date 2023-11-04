import socket

# Create a new socket object
# AF_INET - IPv4 address family
# SOCK_DGRAM - UDP socket type
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Store server address
server_addr = ("localhost", 9090)

# Send bytes to the server address
sock.sendto(b"Hello, Server!", server_addr)

# Wait for server reply
data = sock.recv(1024)

# Print received data
print(data.decode())
