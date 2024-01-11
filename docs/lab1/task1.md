## Задание 1 
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP

### client.py
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_adress = ('localhost', 7777)
conn.connect(server_adress)

conn.send(b"Hello, server")

data = conn.recv(1024)
print(data.decode("utf-8"))

conn.close()
```
### server.py
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_adress = ('localhost', 7777)

conn.bind(server_adress)
data, address = conn.recvfrom(1024)

print(data.decode("utf-8"))
conn.sendto(b"Hello, client", address)

conn.close()
```
![Задание1](img/task1.png)