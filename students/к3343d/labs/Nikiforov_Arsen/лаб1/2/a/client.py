import socket

# Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Подключаемся к серверу
client_socket.connect(server_address)
print("Подключено к серверу...")

# Вводим параметры для теоремы Пифагора (длины катетов) с клавиатуры
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

# Отправляем параметры серверу
message = f"{a},{b}"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print(f"Ответ от сервера: {response.decode()}")

# Закрываем соединение с сервером
client_socket.close()
