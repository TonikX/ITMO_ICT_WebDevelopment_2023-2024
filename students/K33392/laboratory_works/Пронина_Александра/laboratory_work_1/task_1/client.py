import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    message = "Hello, server"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(), (server_ip, server_port))

    response, _ = client_socket.recvfrom(1024)
    print("Response from server:", response.decode())

    client_socket.close()


if __name__ == "__main__":
    main()
