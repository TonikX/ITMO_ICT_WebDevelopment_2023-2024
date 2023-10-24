import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 44455


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "Hello, server"
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    data, addr = client_socket.recvfrom(1024)
    print(f"Получено сообщение от {addr}: {data.decode()}")


if __name__ == "__main__":
    main()