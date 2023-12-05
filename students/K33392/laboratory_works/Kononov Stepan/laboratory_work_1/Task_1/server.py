import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 12345)

    server_socket.bind(server_address)

    print('Сервер запущен и ждет сообщений от клиента...')

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            print(f'Получено сообщение от клиента: "{message}"')

            response_message = 'Hello, client'
            server_socket.sendto(response_message.encode('utf-8'), client_address)
            print('Отправлено сообщение клиенту: "Hello, client"')
    except KeyboardInterrupt:
        print('Сервер остановлен.')


if __name__ == "__main__":
    main()
