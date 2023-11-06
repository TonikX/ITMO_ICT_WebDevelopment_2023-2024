import socket

# Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP-адрес и порт сервера
server_address = ('localhost', 12345)

# Отправляем сообщение серверу
message_to_server = 'Привет, сервер!'
client_socket.sendto(message_to_server.encode(), server_address)

# Ждем ответное сообщение от сервера
data, server_address = client_socket.recvfrom(1024)

# Выводим полученное сообщение от сервера
print(f'Получено от сервера: {data.decode()}')

# Закрываем соединение
client_socket.close()
