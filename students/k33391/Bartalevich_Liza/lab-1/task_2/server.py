import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(2)
    print(f"Server is running on http://localhost:9999")

    while True:
        client, address = server.accept()
        a, b = client.recv(1024).decode('utf-8').split(',')
        data = str(int(a) * int(b))
        print(data)
        client.send(data.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()


