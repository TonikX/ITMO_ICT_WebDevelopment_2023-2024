Title: UDP Client

## Формулировка задания

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение `Hello, server`. Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение `Hello, client`. Сообщение должно
отобразиться у клиента.


## Задаем параметры сервера 
```python
DEST = ("localhost", 1234)
BUFFER_SIZE = 2 ** 20
```
`DEST` - адрес и порт сервера
## Отправка запроса на сервер и обработка ответа
```python
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello from client", DEST)
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    decoded = data.decode("UTF-8")
    print(decoded)
```
Клиент оправляет сообщение `Hello from client` на сервер и ожидает ответа. 
Далее, после получения ответа, он выводится на экран
