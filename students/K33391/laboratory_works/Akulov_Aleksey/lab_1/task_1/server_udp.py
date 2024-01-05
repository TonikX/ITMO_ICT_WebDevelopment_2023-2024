import socket

IP = "127.0.0.1"
PORT = 44455


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP, PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Получено сообщение от {addr}: {data.decode()}")

        response = "Hello, client"
        server_socket.sendto(response.encode(), addr)


if __name__ == "__main__":
    main()