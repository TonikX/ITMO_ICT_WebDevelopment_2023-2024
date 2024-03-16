# Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.

Использовать библиотеку socket.

Реализовать с помощью протокола UDP.

# Выполнение
### Cерверная часть

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    print('Ожидание сообщения от клиента...')
    data, client_address = server_socket.recvfrom(1024)
    print(f'Получено от клиента: {data.decode()}')
    response_message = 'Привет, клиент!'
    server_socket.sendto(response_message.encode(), client_address)
```

Создает UDP-сервер, который привязывается к локальному хосту и порту 12345 и ожидает сообщения от клиента. Когда сервер получает сообщение, он декодирует его, выводит в консоль, формирует ответное сообщение "Привет, клиент!", кодирует его и отправляет обратно клиенту.


### Клиентская часть
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
message_to_server = 'Привет, сервер!'
client_socket.sendto(message_to_server.encode(), server_address)
data, server_address = client_socket.recvfrom(1024)
print(f'Получено от сервера: {data.decode()}')
client_socket.close()
```

Данный код представляет собой простого UDP-клиента на Python, использующего модуль socke
t. Он создает UDP-сокет и отправляет сообщение "Привет, сервер!" на заданный адрес
(localhost, порт 12345). Затем клиент ожидает ответ от сервера и выводит полученны
е данные в консоль, после чего закрывает соединение. Этот код демонстрирует базовую л
огику работы UDP-клиента для обмена данными с сервером без установления постоянного со
единения.Пример работы программы

![Пример изображения](Снимок%20экрана%202024-03-16%20141327.png)

![Пример изображения](Снимок%20экрана%202024-03-16%20141421.png)
