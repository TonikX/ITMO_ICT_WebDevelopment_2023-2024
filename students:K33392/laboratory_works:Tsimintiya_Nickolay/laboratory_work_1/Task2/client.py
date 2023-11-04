from socket import *
from Lab1.serverConfigurator import *

host_configuration = ServerConfigurator()
host = host_configuration.default_configuration()

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(host)

hello_message = client_socket.recv(1024).decode()

print(hello_message)
input = input()

client_socket.sendall(input.encode())

answer = client_socket.recv(1024).decode()
print(answer)