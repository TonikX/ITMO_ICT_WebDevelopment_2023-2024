from Lab1.serverConfigurator import *
from socket import *

configuration = ServerConfigurator()
host = configuration.default_configuration()
client_socket = socket(AF_INET, SOCK_DGRAM)

client_socket.sendto(b"Hello, server!", host)
server_message = client_socket.recvfrom(1024)
message_info = server_message[0].decode()
print(message_info)