import socket

# Using UDP connection (SOCK_DGRAM)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 9090)

try:
    client.sendto(b"Hello, server", server_address)
    data, server = client.recvfrom(1024)
    print(f"Got message from server: {data.decode()}")
finally:
    client.close()
