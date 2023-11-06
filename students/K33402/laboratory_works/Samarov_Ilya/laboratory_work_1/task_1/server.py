import socket

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к IP-адресу и порту
server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    print('Ожидание сообщения от клиента...')
    data, client_address = server_socket.recvfrom(1024)

    # Выводим полученное сообщение от клиента
    print(f'Получено от клиента: {data.decode()}')

    # Отправляем ответное сообщение клиенту
    response_message = 'Привет, клиент!'
    server_socket.sendto(response_message.encode(), client_address)
