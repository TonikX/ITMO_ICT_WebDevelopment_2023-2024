import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1245)
client_socket.connect(server_address)

request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client_socket.send(request.encode())

response = client_socket.recv(1024).decode()

print(response)

client_socket.close()
