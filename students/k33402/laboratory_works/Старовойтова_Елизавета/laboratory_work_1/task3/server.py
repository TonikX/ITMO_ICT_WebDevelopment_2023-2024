import socket

serverAddressPort = ("127.0.0.1", 8100)
bufferSize = 1024

tcpServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to address and IP
tcpServerSock.bind(serverAddressPort)

# listen() puts the socket into server mode, and accept() waits for an incoming connection
tcpServerSock.listen(10)
while True:
    connection, clientAddress = tcpServerSock.accept()
    print(f"Connected by {clientAddress}")
    with connection:
        with open("index.html", "r") as f:
            html = f.read()
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html}"
        connection.sendall(response.encode())
