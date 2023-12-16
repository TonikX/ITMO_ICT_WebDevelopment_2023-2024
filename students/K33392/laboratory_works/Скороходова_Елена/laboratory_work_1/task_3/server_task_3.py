import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    sock.bind(('localhost', 555))  # связь сокета с хостом и портом
    print('Сервер запущен и ожидает входящих данных...')
    sock.listen(5)

    while True:
        try:
            client, addr = sock.accept()
            client.recv(1000)
            response_type = 'HTTP/1.0 200 OK\n'
            headers = 'Contenp-Type: text/html\n\n'
            with open("index.html", "r") as f:
                body = f.read()
            res = response_type + headers + body
            client.send(res.encode('utf-8'))
            client.close()
        except KeyboardInterrupt:
            sock.close()



if __name__ == "__main__":
    main()
