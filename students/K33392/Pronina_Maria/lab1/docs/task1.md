#Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента. Реализовать с помощью протокола UDP.

###Реализация сервера
```python
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('localhost', 44444)) # создание сокета и привязка к хосту и порту

while True:
    data, address = socket.recvfrom(128) # получение данных от клиента
    data = data.decode()
    print(f'Message from {address[0]}:{address[1]}: {data}')
    # обработка сообщения
    if data == 'Hello, server':
        socket.sendto('Hello, client'.encode(), address)
    elif data == 'exit':
        break
    else:
        socket.sendto('No understanding'.encode(), address)

socket.close()
```

###Реализация клиента
```python
import socket

server_address = ('localhost', 44444) # адрес сервера
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #создание сокета

while True:
    msg = input() # чтение сообщения из командной строки
    socket.sendto(msg.encode(), server_address) # отправка сообщения на сервер
    if msg == 'exit':
        break
    else:
        # получение ответа
        data, address = socket.recvfrom(128)
        data = data.decode()
        print(data)

socket.close()
```

###Пример работы
![Пример задания 1](images/task1.png)
![Пример задания 1](images/task1_2.png)