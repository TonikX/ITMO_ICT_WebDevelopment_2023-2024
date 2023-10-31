import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 65432        # Выбранный порт

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))    # Привязываем сокет к адресу и порту
    print('Server started...')
    while True:
        data, addr = s.recvfrom(1024)  # Получаем данные от клиента
        print('Received from client:', data.decode())
        s.sendto(b'Hello, client', addr)  # Отправляем ответ клиенту