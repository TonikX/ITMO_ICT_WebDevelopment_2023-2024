import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 9090))

request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
client.send(request.encode())

response = client.recv(1024)

print(response.decode())

client.close()