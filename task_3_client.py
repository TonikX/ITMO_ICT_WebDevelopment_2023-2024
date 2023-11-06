import socket

# Создаем сокет TCP
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
s_address = ('localhost', 12345)

# Подключаемся к серверу
c_socket.connect(s_address)

try:
    # Отправляем HTTP-запрос
    http_request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
    c_socket.sendall(http_request.encode())

    # Получаем и выводим ответ от сервера
    response = ''
    while True:
        data = c_socket.recv(1024)
        if not data:
            break
        response += data.decode()

    # Отделяем тело HTTP-ответа от заголовков
    body_start = response.find('\r\n\r\n') + 4
    http_body = response[body_start:]

    print(http_body)
except Exception as e:
    print(f'Ошибка при получении HTML-страницы: {str(e)}')
finally:
    # Закрываем сокет клиента
    c_socket.close()

