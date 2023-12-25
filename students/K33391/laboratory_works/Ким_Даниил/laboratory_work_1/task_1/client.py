import socket

# Create a new socket object
# AF_INET - IPv4 address
# SOCK_DGRAM - UDP socket type
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define server address and server port
server_addr = ("localhost", 9090)

# send data to the server
conn.sendto(b"Hello, server", server_addr)

# get response from the server
data = conn.recv(1024)
print(data.decode())

# close connection
conn.close()
