import socket

def main():
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес и порт сервера
    server_address = ('localhost', 12345)

    # Отправляем сообщение серверу
    message = 'Hello, server'
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Ждем получение ответного сообщения от сервера
    data, address = client_socket.recvfrom(1024)

    # Декодируем полученные данные
    response = data.decode('utf-8')

    # Выводим полученное сообщение от сервера
    print('Получен ответ от сервера:', response)

if __name__ == '__main__':
    main()