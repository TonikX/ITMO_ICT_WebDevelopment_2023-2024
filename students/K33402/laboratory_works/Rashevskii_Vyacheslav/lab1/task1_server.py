if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 9090))
    data, address = sock.recvfrom(1024)  # getting client's message

    print(data.decode("utf-8"))
    sock.sendto(b"Hello, client", address)  # send data to client

    sock.close()
