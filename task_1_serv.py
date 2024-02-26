import socket

# Создаем сокет UDP
s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к адресу и порту
s_address = ('localhost', 12345)
s_socket.bind(s_address)

print('Сервер ожидает сообщения...')

while True:
    # Получаем данные от клиента
    data, c_address = s_socket.recvfrom(1024)
    udata = data.decode()
    print(f'Получено сообщение от {c_address}: ' + udata)

    # Отправляем ответ клиенту
    response = 'Hello, client'
    s_socket.sendto(response.encode(), c_address)
