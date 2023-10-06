import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9090))
server.listen(5)

while True:
    client_socket, addr = server.accept()

    try:
        m = float(client_socket.recv(1024).decode())
        h = float(client_socket.recv(1024).decode())

        res = m * h

        client_socket.send(str(res).encode("utf-8"))
    except Exception as e:
        client_socket.send(f"Error {e}".encode())

    client_socket.close()


