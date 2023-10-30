import socket

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем адрес и порт, на котором сервер будет слушать
server_address = ('localhost', 12345)

# Привязываем сервер к адресу и порту
server_socket.bind(server_address)

# Начинаем слушать клиентские запросы (максимум 5 одновременных подключений)
server_socket.listen(5)
print("Сервер запущен и ждет клиентов...")

while True:
    # Ожидаем подключение клиента
    client_socket, client_address = server_socket.accept()
    print(f"Подключено клиентом {client_address}")

    # Принимаем данные от клиента
    data = client_socket.recv(1024)
    print(f"Получено от клиента: {data.decode()}")

    # Разбираем полученные данные (параметры для теоремы Пифагора)
    params = data.decode().split(',')
    a = float(params[0])
    b = float(params[1])

    # Вычисляем гипотенузу (результат теоремы Пифагора)
    c = (a**2 + b**2)**0.5

    # Отправляем результат обратно клиенту
    response = f"Гипотенуза (c) равна: {c}"
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
