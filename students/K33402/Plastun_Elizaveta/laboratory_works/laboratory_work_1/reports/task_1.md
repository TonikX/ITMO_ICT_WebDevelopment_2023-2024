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
<img width="490" alt="image" src="https://github.com/elizavetaplastun/ITMO_ICT_WebDevelopment_2023-2024/assets/71229447/29c60d99-2b64-4c61-8917-4217e84d8c2a">
<img width="447" alt="image" src="https://github.com/elizavetaplastun/ITMO_ICT_WebDevelopment_2023-2024/assets/71229447/11c9a855-a130-41c1-9616-a2495ee0ecce">




