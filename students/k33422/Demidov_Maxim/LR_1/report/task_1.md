## Задача №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает 
серверу сообщение “Hello, server”. Сообщение должно отразиться на 
сервере.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение 
должно отобразиться у клиента.
Обязательно использовать библиотеку socket.
Реализовать с использованием протокола UDP.

## Решение

1. Сервер

```
import socket

def main():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print('Сервер запущен и ожидает сообщения от клиента.')

    while True:
        # Ждем получение сообщения от клиента
        data, address = server_socket.recvfrom(1024)

        # Декодируем полученные данные
        message = data.decode('utf-8')

        # Выводим полученное сообщение от клиента
        print('Получено сообщение от клиента:', message)

        # Отправляем ответное сообщение клиенту
        response = 'Hello, client'
        server_socket.sendto(response.encode('utf-8'), address)

if __name__ == '__main__':
    main()
```
2. Клиент

```
import socket

def main():
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес и порт сервера
    server_address = ('localhost', 12345)

    # Отправляем сообщение серверу
    message = 'Hello, server'
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Ждем получение ответного сообщения от сервера
    data, address = client_socket.recvfrom(1024)

    # Декодируем полученные данные
    response = data.decode('utf-8')

    # Выводим полученное сообщение от сервера
    print('Получен ответ от сервера:', response)

if __name__ == '__main__':
    main()
```

## Пример работы программы

**Серверная и клиентская части**![task1.png](task1.png)