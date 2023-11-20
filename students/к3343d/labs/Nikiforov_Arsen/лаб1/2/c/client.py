import socket

# Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Подключаемся к серверу
client_socket.connect(server_address)

# Запрашиваем параметры трапеции у пользователя
base1 = float(input("Введите длину первого основания трапеции: "))
base2 = float(input("Введите длину второго основания трапеции: "))
height = float(input("Введите высоту трапеции: "))

# Отправляем параметры серверу
message = f"{base1},{base2},{height}"
client_socket.send(message.encode())

# Получаем результат от сервера
result = client_socket.recv(1024).decode()

# Выводим результат
print(f"Площадь трапеции: {result}")

# Закрываем сокет клиента
client_socket.close()
