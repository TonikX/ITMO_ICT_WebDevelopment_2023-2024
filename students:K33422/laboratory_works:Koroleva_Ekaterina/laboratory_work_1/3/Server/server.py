from socket import *

# Настраиваем хост
host = gethostname()
port = 10000
host_data = (host, port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(host_data)
server_socket.listen()

conn, addr = server_socket.accept()
request = conn.recv(4096)

file = open("index.html", "r")
file_data = file.read()

header = b"HTTP/1.1 200\r\nserver: localhost\r\ncontent-type: text/html\r\ncharset=UTF-8\r\n\r\n"
body = file_data.encode()
response = header + body
conn.sendall(response)
conn.close()


