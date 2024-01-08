import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 9090)
server.bind(server_address)

while True:
    data, client_address = server.recvfrom(1024)
    print(f"Got message from client: {data.decode()}")
    server.sendto(b"Hello, client", client_address)
