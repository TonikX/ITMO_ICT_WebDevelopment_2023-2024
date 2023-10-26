import socket

MESSAGE = 'Hello, Client'


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 9090))

    while True:
        data, addr = sock.recvfrom(1024)

        print(data.decode('utf-8'))

        sock.sendto(MESSAGE.encode('utf-8'), addr)


if __name__ == '__main__':
    run()
