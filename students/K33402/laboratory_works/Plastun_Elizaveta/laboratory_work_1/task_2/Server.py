import socket


def area_of_parallelogram(a, b):
    return str(a * b)


servers_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servers_sockets.bind((socket.gethostname(), 6666))
servers_sockets.listen(5)

while True:
    client_socket, addr = servers_sockets.accept()
    data = client_socket.recv(1024).decode()

    a, b = map(float, data.split(" "))
    rezult = area_of_parallelogram(a, b)

    serverMessage = f"area of parallelogram with height = {a} and side = {b} is {rezult}"

    client_socket.send(serverMessage.encode("utf-8"))
    if False:
        break

servers_sockets.close()
