import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))

    while True:

        data, client_address = server_socket.recvfrom(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Received message from {client_address}: {message}")
            server_socket.sendto("Hello client!".encode("utf-8"), client_address)


if __name__ == "__main__":
    main()