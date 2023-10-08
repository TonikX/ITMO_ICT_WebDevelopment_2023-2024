import socket

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
server_address = ('localhost', 12345)

# Привязываем сокет к адресу и порту
server_socket.bind(server_address)

# Слушаем входящие соединения
server_socket.listen(1)

print("Сервер запущен и ожидает подключений...")

while True:
    # Принимаем входящее подключение
    client_socket, client_address = server_socket.accept()
    
    # Выводим информацию о клиенте
    print(f"Подключение от клиента ({client_address})")
    
    # Получаем данные от клиента
    data = client_socket.recv(1024).decode()
    
    # Разбираем полученные данные (длины оснований и высоту)
    base1, base2, height = map(float, data.split(','))
    
    # Вычисляем площадь трапеции
    area = 0.5 * (base1 + base2) * height
    
    # Отправляем результат клиенту
    client_socket.send(str(area).encode())
    
    # Закрываем сокет клиента
    client_socket.close()
