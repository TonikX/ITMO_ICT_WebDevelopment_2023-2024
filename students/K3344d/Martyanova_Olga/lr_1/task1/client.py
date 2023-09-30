import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9090)
client_socket.connect(server_address)

message = 'Hello, server'
client_socket.send(message.encode('utf-8'))

response = client_socket.recv(1024)
response_message = response.decode('utf-8')

print(f'Received message from server: "{response_message}"')

client_socket.close()

