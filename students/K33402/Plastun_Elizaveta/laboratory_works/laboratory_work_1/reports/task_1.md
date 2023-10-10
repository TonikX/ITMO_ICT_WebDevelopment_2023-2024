#  🗿 Задача 1 
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.

## 🥸 Реализация
1. Server.py
   
   ```python
   import socket

   servers_sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   servers_sockets.bind((socket.gethostname(), 6666))
   
   while True:
       clientMessage, addr = servers_sockets.recvfrom(1024)
       print(f"Client says: {clientMessage.decode()}")
       serverMessage = "Hello Client!"
       servers_sockets.sendto(serverMessage.encode("utf-8"), addr)
       if False:
           break

   servers_sockets.close()

2. Client.py
```python
import socket

clients_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clients_socket.connect((socket.gethostname(), 6666))

clients_socket.send("Hello Server!".encode())

serverMessage, addr = clients_socket.recvfrom(1024)

print(f"Server says: {serverMessage.decode()}")

clients_socket.close()
```

## 🤡 Демонстрация работы




