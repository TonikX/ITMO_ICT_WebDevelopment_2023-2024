import socket

# Create a new socket object
# AF_INET - IPv4 address
# SOCK_DGRAM - UDP socket type
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind server address and server port
conn.bind(("localhost", 9090))

# get data and IP address from the client
data, client_addr = conn.recvfrom(1024)

# decode and print client data
udata = data.decode()
print(udata)

# send response to the client
conn.sendto(b"Hello, client", client_addr)

# close connection
conn.close()