#  🗿 Задача 2 
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера выполнение математической операции, параметры, которые вводятся с клавиатуры. Сервер обрабатывает полученные данные и возвращает результат клиенту. Вариант: Поиск площади параллелограмма.

## 🥸 Реализация
1. Server.py
   
```python
   servers_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servers_sockets.bind((socket.gethostname(), 6666))
servers_sockets.listen(5)

while True:
    client_socket, addr = servers_sockets.accept()
    data = client_socket.recv(1024).decode()

    a, b = map(float, data.split(" "))
    rezult = area_of_parallelogram(a, b)

    serverMessage = f"area of parallelogram with height = {a} and side = {b} is {rezult}"

    client_socket.send(serverMessage.encode("utf-8"))
    if False:
        break

servers_sockets.close()
```

2. Client.py
```python
import socket

clients_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients_socket.connect((socket.gethostname(), 6666))

a = input("enter the height of the parallelogram:\n")
b = input("enter the parallelogram edge value:\n")
data = a + " " + b
print(type(data))
clients_socket.send(data.encode())

serverMessage, addr = clients_socket.recvfrom(1024)

print(f"Server says: {serverMessage.decode()}")

clients_socket.close()

```

## 🤡 Демонстрация работы
![client_task_2.png](/Users/elizaveta/ITMO_ICT_WebDevelopment_2023-2024/students/K33402/Plastun_Elizaveta/laboratory_works/laboratory_work_1/reports/img/client_task_2.png)
