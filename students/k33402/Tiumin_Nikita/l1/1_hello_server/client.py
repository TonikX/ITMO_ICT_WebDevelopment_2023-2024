import socket

MESSAGE = 'Hello, Server'


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(MESSAGE.encode('utf-8'), ('localhost', 9090))

    message, addr = sock.recvfrom(1024)

    print(message.decode('utf-8'))


if __name__ == '__main__':
    run()
