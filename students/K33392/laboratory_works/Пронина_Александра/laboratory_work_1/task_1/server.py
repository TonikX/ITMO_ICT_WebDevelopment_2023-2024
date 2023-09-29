import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print("Server is listening on", server_ip, "port", server_port)

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print("Message from client:", message.decode())

        response = "Hello, client"
        server_socket.sendto(response.encode(), client_address)


if __name__ == "__main__":
    main()
