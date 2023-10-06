import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9090))
server.listen(5)

while True:
    client_socket, addr = server.accept()

    with open('index.html') as html:
        html_content = html.read()

    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
    client_socket.send(response.encode())

    client_socket.close()