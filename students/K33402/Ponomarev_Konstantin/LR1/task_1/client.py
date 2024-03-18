import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ("localhost", 9090)

    message = b"Hello, server"

    try:
        _socket.sendto(message, server_address)
        data = _socket.recv(1024)
        print(f"Server answered: {data.decode()}")

    finally:
        _socket.close()


if __name__ == '__main__':
    init_socket()
