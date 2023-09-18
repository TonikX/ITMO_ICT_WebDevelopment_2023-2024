import socket

# Создаем сокет для TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Начинаем слушать порт
server_socket.listen(1)
print("Сервер запущен и слушает на порту 12345...")

while True:
    # Принимаем подключение от клиента
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()
    print(f"Подключено клиентом {client_address}")

    # Принимаем данные от клиента
    data = client_socket.recv(1024)
    message = data.decode()
    print(f"Получено от клиента: {message}")

    # Разбираем полученные данные
    try:
        sides = message.split(',')
        if len(sides) == 2:
            a = float(sides[0])
            b = float(sides[1])
            # Вычисляем площадь параллелограмма
            area = a * b
            response = f"Площадь параллелограмма: {area}"
        else:
            response = "Ошибка: Введите две стороны через запятую (например, 5, 7)."
    except ValueError:
        response = "Ошибка: Введите числовые значения для сторон."

    # Отправляем ответ клиенту
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
