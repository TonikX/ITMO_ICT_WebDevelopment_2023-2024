import socket

server = socket.socket()
server.bind(('', 9090))
server.listen(1)
conn, addr = server.accept()

data = conn.recv(1024)
print(data.decode('utf-8'))
conn.sendto('Hello, client'.encode('utf-8'), addr)

conn.close()
