import socket

def main():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print('Сервер запущен и ожидает сообщения от клиента.')

    while True:
        # Ждем получение сообщения от клиента
        data, address = server_socket.recvfrom(1024)

        # Декодируем полученные данные
        message = data.decode('utf-8')

        # Выводим полученное сообщение от клиента
        print('Получено сообщение от клиента:', message)

        # Отправляем ответное сообщение клиенту
        response = 'Hello, client'
        server_socket.sendto(response.encode('utf-8'), address)

if __name__ == '__main__':
    main()