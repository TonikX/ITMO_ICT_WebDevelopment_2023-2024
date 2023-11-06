import socket

# Функция для чтения содержимого файла
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не найден"


# Создаем сокет TCP
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
s_address = ('localhost', 12345)
s_socket.bind(s_address)

# Ожидаем соединения клиента
s_socket.listen(1)
print('Сервер ожидает подключения клиента...')

while True:
    # Принимаем соединение от клиента
    c_socket, c_address = s_socket.accept()
    print(f'Подключено клиентом {c_address}')

    try:
        # Читаем содержимое файла index.html
        html_content = read_file('index.html')
        c_socket.recv(1024)
        # Создаем HTTP-ответ с HTML-страницей
        http_response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"

        # Отправляем HTTP-ответ клиенту
        c_socket.sendall(http_response.encode())
    except Exception as e:
        print(f'Ошибка: {str(e)}')
    finally:
        # Закрываем соединение с клиентом
        c_socket.close()
