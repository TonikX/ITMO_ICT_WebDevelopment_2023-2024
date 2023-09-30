import socket

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

request = "GET / HTTP/1.1\r\nHost: %s" % IP
client_socket.sendall(request.encode(codage))

result = client_socket.recv(1024).decode(codage)

print(result)

client_socket.close()