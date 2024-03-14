import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _socket.bind(("localhost", 9090))
    print("socket bound, wait messages...")
    while True:
        data, client_address = _socket.recvfrom(1024)
        parsed_data = data.decode()
        print(f"Message from client: {parsed_data}")

        response = b"Hello, client"
        _socket.sendto(response, client_address)


if __name__ == '__main__':
    init_socket()
