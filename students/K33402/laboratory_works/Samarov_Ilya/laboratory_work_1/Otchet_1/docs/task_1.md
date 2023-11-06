#  Задание №1
___
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
## Реализация
server.py

```python
import socket

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к IP-адресу и порту
server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    print('Ожидание сообщения от клиента...')
    data, client_address = server_socket.recvfrom(1024)

    # Выводим полученное сообщение от клиента
    print(f'Получено от клиента: {data.decode()}')

    # Отправляем ответное сообщение клиенту
    response_message = 'Привет, клиент!'
    server_socket.sendto(response_message.encode(), client_address)
```

client.py

```python
import socket

# Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP-адрес и порт сервера
server_address = ('localhost', 12345)

# Отправляем сообщение серверу
message_to_server = 'Привет, сервер!'
client_socket.sendto(message_to_server.encode(), server_address)

# Ждем ответное сообщение от сервера
data, server_address = client_socket.recvfrom(1024)

# Выводим полученное сообщение от сервера
print(f'Получено от сервера: {data.decode()}')

# Закрываем соединение
client_socket.close()
```

## Результаты 
![results](Task1client.png)
![results](Task1server.png)
