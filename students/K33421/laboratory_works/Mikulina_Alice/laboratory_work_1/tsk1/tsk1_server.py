import socket

server_ip = 'localhost'
server_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((server_ip, server_port))

print('Server listening on', server_ip, server_port)

while True:
    data, client_address = sock.recvfrom(4096)
    message = data.decode()

    print('Received message from client:', message)
    
    response = 'Hello, client!'
    sock.sendto(response.encode(), client_address)