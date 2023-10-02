import socket

# Имя и порт сервера
server_address = ('localhost', 12345)
buffer_size = 1024

# Создаем UDP-сокет клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Отправляем сообщение серверу
client_message = 'Hello, server'
client_socket.sendto(client_message.encode('utf-8'), server_address)

# Получаем ответное сообщение от сервера
server_message, server_address = client_socket.recvfrom(buffer_size)
server_message = server_message.decode('utf-8')
print('Сообщение от сервера:', server_message)

# Закрываем UDP-сокет клиента
client_socket.close()


