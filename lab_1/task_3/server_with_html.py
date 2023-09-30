import socket
import math

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(10)

while True:
    try:
        outer_socket, addr = server_socket.accept()
        request = outer_socket.recv(1024).decode(codage)
        print(request)

        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        with open("index.html", "r") as f:
            body = f.read()

        response = response_type + headers + body
        outer_socket.send(response.encode(codage))
        outer_socket.close()
    except KeyboardInterrupt:
        server_socket.close()
        break
