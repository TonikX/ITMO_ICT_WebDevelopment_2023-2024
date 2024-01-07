## Задание 2 
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Вариант: Поиск площади трапеции.

### client.py
import socket
import json

a = int(input("Введите первое основание трапеции: "))
b = int(input("Введите второе основание трапеции: "))
h = int(input("Введите высоту трапеции: "))

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 7777)
conn.connect(server_address)

conn.send(json.dumps({"a": a, "b": b, "h": h}).encode("utf-8"))

data = conn.recv(1024)

print("Площадь трапеции: " + data.decode("utf-8"))

conn.close()

### server.py

import socket 
import json

def trapez_area_count(a, b, h):
    area = ((a+b)*h)/2
    return area

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7777)

conn.bind(server_address)
conn.listen()

connect, address = conn.accept()

while True:
    data = connect.recv(1024)
    if not data:
        break
    vars = json.loads(data.decode())
    connect.send(str(trapez_area_count(**vars)).encode("utf-8"))

connect.close()

[Задание2](task2.png)