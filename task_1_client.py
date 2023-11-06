import socket

# Создаем сокет UDP
c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Адрес и порт сервера
s_address = ('localhost', 12345)

# Отправляем сообщение серверу
message = 'Hello, server'
c_socket.sendto(message.encode(), s_address)

# Получаем ответ от сервера
data, s_address = c_socket.recvfrom(1024)
udata = data.decode()
print(f'Получен ответ от сервера: ' + udata)

# Закрываем сокет клиента
c_socket.close()
