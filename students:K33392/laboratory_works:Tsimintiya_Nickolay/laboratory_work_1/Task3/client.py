from socket import *
from Lab1.serverConfigurator import ServerConfigurator

server_config = ServerConfigurator()
host = server_config.default_configuration()
client = socket(AF_INET, SOCK_STREAM)

client.connect(host)
request = b"GET / HTTP/1.1\r\nHost: localhost\r\nAccept: text/html\r\nConnection: close\r\n\r\n"
client.sendall(request)
file_data = client.recv(4096)
print(file_data.decode())
