#!/usr/bin/python
import socket

host = socket.gethostname()
port = 12355

server = socket.socket()
server.bind((host, port))

print("Starting server on", host, port)

server.listen(5)

while True:
    client, (client_host, client_port) = server.accept()
    print("Get connection from", client_host, client_port)
    client.recv(1000)
    response_type = "HTTP/1.0 200 OK\n"
    headers = "Content-Type: text/html\n\n"
    file = open("/Users/aleksejrevakin/Desktop/Itmo-33392/web/Lab_1/3/index.html", "r")
    body = file.read()
    file.close
    response = response_type + headers + body
    client.send(response.encode("utf-8"))
    client.close()
