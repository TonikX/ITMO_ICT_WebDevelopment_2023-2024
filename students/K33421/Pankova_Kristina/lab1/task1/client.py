import socket

HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Выбранный порт

# Создаем сокет и подключаемся к серверу
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, server', (HOST, PORT))  # Отправляем сообщение серверу
    data, addr = s.recvfrom(1024)         # Получаем ответ от сервера
    print('Received from server:', data.decode())
