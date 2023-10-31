from socket import *

HOST = (gethostname(), 10000)
client = socket(AF_INET, SOCK_STREAM)

client.connect(HOST)
request = b"GET / HTTP/1.1\r\nHost: localhost\r\nAccept: text/html\r\nConnection: close\r\n\r\n"
client.sendall(request)
file_data = client.recv(4096)
print(file_data.decode())