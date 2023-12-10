if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('localhost', 9090))
    sock.send(b"Hello, server")  # sending message

    msg = sock.recv(1024)  # getting server's message
    print(msg.decode("utf-8"))  # printing server's message
    sock.close()
