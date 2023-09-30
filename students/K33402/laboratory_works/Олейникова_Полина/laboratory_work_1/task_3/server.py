import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))
sock.listen()
print("Server is running on http://localhost:9090")

while True:
    connection, address = sock.accept()

    data = connection.recv(1024)
    if not data:
        break

    print(data.decode("utf-8"))

    content = open("index.html").read()
    response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content

    connection.send(response.encode("utf-8"))
    connection.close()
