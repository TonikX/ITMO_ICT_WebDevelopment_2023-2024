if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9090))

    http_request = "GET / HTTP/1.1\r\nHost: localhost:9090\r\n\r\n"
    sock.send(http_request.encode('utf-8'))

    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))

    sock.close()
