import socket

# Создаем сокет для UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Сообщение для отправки серверу
message = "Hello, server"

# Отправляем сообщение серверу
client_socket.sendto(message.encode(), server_address)

# Принимаем ответ от сервера
data, _ = client_socket.recvfrom(1024)

# Выводим полученный ответ от сервера
print(f"Получено от сервера: {data.decode()}")

# Закрываем сокет клиента
client_socket.close()
