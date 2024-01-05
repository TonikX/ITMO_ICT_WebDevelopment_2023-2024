import math
import socket
import json

def tcp_server(host, port):
    # Create server socket and put it into listening mode
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()

        # Receive a message from the client
        data = client_socket.recv(1024).decode()

        # Parse the message
        # The message is a json object containing a list
        # of three parameters of the quadratic equation
        parameters = json.loads(data)
        a = parameters[0]
        b = parameters[1]
        c = parameters[2]

        # Solve quadratic equation
        solutions = solve_equation(a, b, c)

        # Convert a list of solutions into a json object
        json_string = json.dumps(solutions)

        # Send json object to the client
        client_socket.send(json_string.encode())

        # Close the connection
        client_socket.close()

def solve_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if (D > 0):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif (D == 0):
        x = -b / (2 * a)
        return (x,)
    else:
        return ()

if __name__ == "__main__":
    host = 'localhost'
    port = 5555
    tcp_server(host, port)