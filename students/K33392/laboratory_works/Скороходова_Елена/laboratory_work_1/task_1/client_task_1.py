import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание сокета
    sock.sendto(b'Hello, server!', ('localhost', 9090))

    data, addr = sock.recvfrom(1024)
    sock.close()
    print(data.decode('utf-8'))


if __name__ == "__main__":
    main()
