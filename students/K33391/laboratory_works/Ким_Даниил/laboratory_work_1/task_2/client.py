import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define server address and server port
server_addr = ("localhost", 9090)

conn.connect(server_addr)

hello_data = conn.recv(1024)
print(hello_data.decode())

conn.send(input().encode())
data = conn.recv(1024)
print(data.decode())

# close connection
conn.close()
