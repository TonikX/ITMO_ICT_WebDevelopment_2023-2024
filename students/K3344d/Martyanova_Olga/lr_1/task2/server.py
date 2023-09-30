import socket
import math

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9090)
server_socket.bind(server_address)

server_socket.listen(1)
print("Server is running. Waiting for a client...")


while True:
    try:
        client_socket, client_address = server_socket.accept()

        try:
            data = client_socket.recv(1024)
            params = data.decode('utf-8').split(',')
            a, b, c = map(float, params)

            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                result = f"x1 = {root1}, x2 = {root2}"
            elif discriminant == 0:
                root1 = -b / (2*a)
                result = f"x1 = {root1}"
            else:
                result = "No real roots"

            client_socket.send(result.encode('utf-8'))
        except ValueError:
            error_message = "Parameters must be numbers"
            client_socket.send(error_message.encode('utf-8'))
    except KeyboardInterrupt:
        server_socket.close()
        print('Connection closed.')
        break
