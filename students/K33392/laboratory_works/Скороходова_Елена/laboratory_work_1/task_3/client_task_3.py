import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    sock.connect(('localhost', 555))
    sock.send(b'Hello, server!')
    data = sock.recv(1024).decode('utf-8')
    print(data)
    sock.close()


if __name__ == "__main__":
    main()
