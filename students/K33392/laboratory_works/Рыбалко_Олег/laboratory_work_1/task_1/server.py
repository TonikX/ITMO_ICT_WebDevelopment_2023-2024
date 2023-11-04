import socket

# Create a new socket object
# AF_INET - IPv4 address family
# SOCK_DGRAM - UDP socket type
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Store server address
server_addr = ("localhost", 9090)

# Bind a socket to a local address
sock.bind(server_addr)

# Receive data and ip address from a client
data, client_addr = sock.recvfrom(1024)
print(data.decode())

# Send a response to the client
sock.sendto(b"Hello, Client!", client_addr)
