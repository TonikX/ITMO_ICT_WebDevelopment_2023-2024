import socket
import math

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'


def solve_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)

    while True:
        try:
            outer_socket, addr = server_socket.accept()
            received_string = outer_socket.recv(1024).decode(codage)

            a, b = map(float, received_string.split())
            result = solve_hypotenuse(a, b)
            outer_socket.send(str(result).encode(codage))
        except KeyboardInterrupt:
            server_socket.close()
            break


if __name__ == "__main__":
    main()