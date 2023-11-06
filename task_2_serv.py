import socket

# Создаем сокет TCP
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
s_address = ('127.0.0.1', 12348)
s_socket.bind(s_address)

# Ожидаем соединений клиента
s_socket.listen(1)
print('Сервер ожидает подключения клиента...')

while True:
    # Принимаем соединение от клиента
    c_socket, c_address = s_socket.accept()
    print(f'Подключено клиентом {c_address}')

    try:
        # Получаем параметры от клиента
        a = float(c_socket.recv(1024).decode())
        b = float(c_socket.recv(1024).decode())

        # Выполняем математическую операцию (теорема Пифагора)
        c = (a ** 2 + b ** 2) ** 0.5

        # Отправляем результат клиенту
        c_socket.send(str(c).encode())
    except ValueError:
        print('Ошибка: Некорректные данные от клиента.')
    finally:
        # Закрываем соединение с клиентом
        c_socket.close()
