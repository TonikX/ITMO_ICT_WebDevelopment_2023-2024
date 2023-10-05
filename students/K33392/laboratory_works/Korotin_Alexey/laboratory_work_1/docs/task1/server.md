Title: UDP Server

## Формулировка задания

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение `Hello, server`. Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение `Hello, client`. Сообщение должно
отобразиться у клиента.

## Задаем параметры сервера 
```python
HOST = "localhost"
PORT = 1234
BUFFER_SIZE = 2 ** 20
```
## Обработка запроса клиента
```python
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    decoded = data.decode("UTF-8")
    print(decoded)
    s.sendto(b"Hello from server", sender_address)
```
Сервер получает сообщение, выводит его на экран. 
Далее отправляет сообщение `Hello from server` на адрес, с которого он получил сообщение