## Задача №2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера выполнение математической операции, параметры которой вводятся с клавиатуры. 
Сервер обрабатывает полученные данные и возвращает результат клиенту. 

Мой вариант, согласно списку группы, – теорема Пифагора.

## Решение

1. Сервер

```
import socket
from math import sqrt


def pyth_theorem(cath1, cath2=None, hyp=None):
    if not (cath1 or hyp) or (hyp and cath1 >= hyp):
        return "Invalid input"
    if not cath2:
        return sqrt(hyp ** 2 - cath1 ** 2)
    if not hyp:
        return sqrt(cath1 ** 2 + cath2 ** 2)
    return "Something went wrong"


if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 6999

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((server_ip, server_port))
    conn.listen()

    conn, addr = conn.accept()
    while True:
        data = conn.recv(1024).decode("utf-8")

        if not data:
            continue

        operation, a, b = data.split(',')
        a, b = float(a), float(b)

        if operation == "hyp":
            result = pyth_theorem(cath1=a, cath2=b)
        elif operation == "cath":
            result = pyth_theorem(cath1=a, hyp=b)
        else:
            result = "Invalid operation"

        conn.send(bytes(str(result), encoding="utf-8"))
```

2. Клиент

```
import socket

if __name__ == "__main__":
    # Задаем IP-адрес и порт сервера, к которому будем подключаться.
    server_ip = '127.0.0.1'
    server_port = 6998

    # Создаем TCP сокет (SOCK_STREAM) и устанавливаем соединение с сервером.
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_ip, server_port))

    # Запрашиваем у пользователя выбор операции (cath/hyp или c/h).
    operation = input("Выберите опцию (cath/hyp или c/h): ")

    # Проверяем, что пользователь ввел корректную операцию.
    while operation not in ["cath", "c", "hyp", "h"]:
        operation = input("Неверная операция. Попробуйте снова: ")

    # Преобразуем сокращенные операции в полные.
    if operation in ("c", "h"):
        operation = "cath" if operation == "c" else "hyp"

    # Вводим значения сторон треугольника с обработкой ошибок.
    while True:
        if operation == "cath":
            a = input("Введите катет: ")
            b = input("Введите гипотенузу: ")
        else:
            a = input("Введите катет: ")
            b = input("Введите катет: ")
        try:
            a = float(a)
            b = float(b)
            break
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")

    # Отправляем операцию и значения сторон на сервер.
    conn.send(bytes(f"{operation}, {a}, {b}", encoding="utf-8"))

    # Получаем и выводим результат от сервера.
    result = conn.recv(1024).decode("utf-8")
    print(f"Результат: {result}")
```

## Демонстрация работы

![Клиентская часть #1](images/task2_client1.png)
![Клиентская часть #2](images/task2_client2.png)
![Клиентская часть #3](images/task2_client3.png)
