import socket

# Имя и порт сервера
server_address = ('localhost', 12345)
buffer_size = 1024

# Создаем UDP-сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

# Ожидаем получение данных от клиента
print('Сервер запущен. Ожидание данных от клиента...')
client_message, client_address = server_socket.recvfrom(buffer_size)
client_message = client_message.decode('utf-8')
print('Сообщение от клиента:', client_message)

# Отправляем ответ клиенту
server_message = 'Hello, client'
server_socket.sendto(server_message.encode('utf-8'), client_address)

# Закрываем UDP-сокет сервера
server_socket.close()