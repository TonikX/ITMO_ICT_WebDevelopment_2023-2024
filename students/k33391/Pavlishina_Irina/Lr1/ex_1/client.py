import socket

"""
    First UDP client code

"""

PORT = 8080


def main():
    """
    Main function of client running.

    Connection to port 8080 on lockalhost and sending "Hello, server" message.

    :return: Nothing
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b'Hello, server', ('localhost', PORT))
    data, addr = sock.recvfrom(1024)
    print(data)


if __name__ == "__main__":
    main()
