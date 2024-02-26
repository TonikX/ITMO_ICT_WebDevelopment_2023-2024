import socket

# Создаем сокет TCP
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
s_address = ('127.0.0.1', 12348)

# Подключаемся к серверу
c_socket.connect(s_address)

try:
    # Вводим параметры с клавиатуры
    a = float(input('Введите значение a: '))
    b = float(input('Введите значение b: '))

    # Отправляем параметры серверу
    c_socket.send(str(a).encode())
    c_socket.send(str(b).encode())

    # Получаем результат от сервера
    result = c_socket.recv(1024).decode()
    print(f'Результат: {result}')
except ValueError:
    print('Ошибка: Введите корректные числовые значения для a и b.')
finally:
    # Закрываем соединение с сервером
    c_socket.close()
