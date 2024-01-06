# task2
В данном документе предоставлена краткая информация о примере кода на Python для реализации TCP клиент-серверной коммуникации. Код включает в себя скрипт клиента и скрипт сервера, которые обмениваются данными и выполняют операции по теореме Пифагора.

## Клиентский Скрипт (client.py)

Скрипт клиента устанавливает соединение с сервером, указанным по IP-адресу и порту. Затем он запрашивает у пользователя выбор операции (нахождение катета или гипотенузы) и значения сторон треугольника. После отправки данных на сервер, клиент получает и выводит результат операции.

```python
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

## Серверный Скрипт (server.py)

Скрипт сервера привязывает сокет к указанному IP-адресу и порту, затем прослушивает входящие соединения от клиентов. Сервер выполняет операции на основе теоремы Пифагора для вычисления катетов и гипотенузы треугольника и отправляет результат обратно клиенту.

```python
import socket
from math import sqrt

# Функция для вычисления катетов и гипотенузы по теореме Пифагора.
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

Теперь вы можете использовать эти скрипты для установки TCP-соединения между клиентом и сервером и выполнения операций по теореме Пифагора.