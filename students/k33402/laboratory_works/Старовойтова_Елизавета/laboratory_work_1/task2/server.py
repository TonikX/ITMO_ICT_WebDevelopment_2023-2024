import socket

serverAddressPort = ("127.0.0.1", 2005)
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
                startMessage = """Для нахождения площади трапеции введите коэффициенты длину верхнего основания, нижнего и высоту через запятую."""
                connection.sendall(startMessage.encode('utf-8'))

                recieved = connection.recv(bufferSize)
                recieved = recieved.decode('utf-8')
                print(f'Client: {recieved}')

                a, b, h = map(float, recieved.split(','))
                result = str((a + b) * h / 2)
                connection.sendall(result.encode("utf-8"))

