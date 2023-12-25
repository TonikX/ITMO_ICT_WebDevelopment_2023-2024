import socket

# Создаем TCP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print("Сервер запущен. Ожидание подключения клиента...")

while True:
    client_connection, client_address = server_socket.accept()
    print(f"Подключение от клиента {client_address}")

    # Принимаем данные от клиента
    data = client_connection.recv(1024).decode()
    print(f"Получено сообщение от клиента: {data}")

    # Разбираем данные и выполняем математическую операцию (теорема Пифагора)
    try:
        a, b = map(float, data.split(','))
        c = (a ** 2 + b ** 2) ** 0.5
        response = f"Гипотенуза (c) равна {c}"
    except ValueError:
        response = "Ошибка: Некорректные данные"

    # Отправляем результат клиенту
    client_connection.send(response.encode())
    client_connection.close()
