import socket

def main():
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес и порт сервера
    server_address = ('localhost', 12345)

    # Вводим параметры a, b, c с клавиатуры
    a = float(input('Введите значение a: '))
    b = float(input('Введите значение b: '))
    c = float(input('Введите значение c: '))

    # Формируем запрос в виде строки "a,b,c"
    request = '{},{},{}'.format(a, b, c)

    # Отправляем запрос серверу
    client_socket.sendto(request.encode('utf-8'), server_address)

    # Ждем получение результата от сервера
    data, address = client_socket.recvfrom(1024)

    # Декодируем полученные данные
    result = data.decode('utf-8')

    # Выводим результат
    print('Результат:', result)

if __name__ == '__main__':
    main()