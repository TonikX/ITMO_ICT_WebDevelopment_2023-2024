import socket

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Привязываем сокет к адресу и порту
server_socket.bind(server_address)

# Начинаем слушать порт
server_socket.listen(1)
print("Сервер запущен и ожидает подключений...")

while True:
    # Принимаем соединение от клиента
    client_socket, client_address = server_socket.accept()
    print(f"Подключено клиентом ({client_address})")

    # Получаем данные от клиента
    data = client_socket.recv(1024)
    coefficients = data.decode().split(',')

    # Извлекаем коэффициенты a, b и c из полученных данных
    a, b, c = map(float, coefficients)

    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    # Решаем квадратное уравнение
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        result = f"Два корня: x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        result = f"Один корень: x = {x}"
    else:
        result = "Нет действительных корней"

    # Отправляем результат клиенту
    client_socket.send(result.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
