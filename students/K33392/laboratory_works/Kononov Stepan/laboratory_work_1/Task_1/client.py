import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 12345)

    message = 'Hello, server'

    try:

        client_socket.sendto(message.encode('utf-8'), server_address)
        print(f'Отправлено сообщение серверу: "{message}"')

        response, _ = client_socket.recvfrom(1024)
        response_message = response.decode('utf-8')
        print(f'Получен ответ от сервера: "{response_message}"')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    finally:

        client_socket.close()


if __name__ == "__main__":
    main()
