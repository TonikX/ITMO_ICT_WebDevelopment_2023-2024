import socket

# Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Подключаемся к серверу
client_socket.connect(server_address)
print("Подключено к серверу...")

# Вводим коэффициенты квадратного уравнения с клавиатуры
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Отправляем коэффициенты серверу
message = f"{a},{b},{c}"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024)
print(f"Ответ от сервера: {response.decode()}")

# Закрываем соединение с сервером
client_socket.close()
