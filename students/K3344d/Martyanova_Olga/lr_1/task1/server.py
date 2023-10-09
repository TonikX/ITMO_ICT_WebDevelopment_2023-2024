import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9090)
server_socket.bind(server_address)

print("Server is running. Waiting for a message...")

data, client_address = server_socket.recvfrom(1024)
message = data.decode('utf-8')
print(f'Received message from client: "{message}"')

response_message = 'Hello, client'
server_socket.sendto(response_message.encode('utf-8'), client_address)

server_socket.close()