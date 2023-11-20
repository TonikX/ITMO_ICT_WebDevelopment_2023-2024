import socket

# Создаем сокет для TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Устанавливаем соединение с сервером
client_socket.connect(server_address)

# Получаем данные от пользователя
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))

# Отправляем данные серверу
message = f"{a},{b}"
client_socket.send(message.encode())

# Получаем ответ от сервера
data = client_socket.recv(1024)
response = data.decode()
print(response)

# Закрываем соединение с сервером
client_socket.close()
