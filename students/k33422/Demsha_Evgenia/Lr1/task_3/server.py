import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 9090))
sock.listen()

while True:
    connection, address = sock.accept()
    connection.recv(2048)
    with open("index.html") as index:
        html_body = index.read()
    response = "HTTP/1.1 200 OK \nContent-Type: text/html \n\n" + html_body
    connection.send(response.encode())    # посылаем ответ клиенту
    connection.close()