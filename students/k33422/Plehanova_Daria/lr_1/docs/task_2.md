# Задание 2

## Описание Задачи

Задача заключается в реализации клиент-серверного приложения на Python с использованием библиотеки `socket`. Клиент
запрашивает у сервера выполнение математической операции — расчет по теореме Пифагора, основываясь на параметрах,
вводимых пользователем. Сервер обрабатывает запрос, выполняет вычисления и возвращает результат клиенту.

## Реализация

### Серверная Часть

Файл: `server.py`

Сервер ожидает подключение клиента, запрашивает данные (значения `a` и `b`), выполняет расчет по теореме Пифагора и
отправляет результат обратно клиенту.

```python
import socket


def pif(a, b):
    return a ** 2 + b ** 2


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        conn.listen()
        while True:
            client_conn, addr = conn.accept()
            with client_conn:
                print(f'Connected by {addr}')
                client_conn.sendall(b'Enter a, b: ')
                data = client_conn.recv(1024)
                data = data.decode()
                try:
                    a, b = map(float, data.split(', '))
                    output = f"{pif(a, b)}"
                except ValueError:
                    output = 'Invalid input'
                client_conn.sendall(output.encode())
```

### Клиентская Часть

Файл: `client.py`

Клиент подключается к серверу, отправляет данные для расчета и ожидает результат от сервера.

```python
import socket

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect(('127.0.0.1', 8888))
        
        data = conn.recv(1024)
        print(data.decode())
        
        data = input()
        conn.sendall(data.encode())
        
        data = conn.recv(1024)
        print(data.decode())
```

## Выводы

Были разработаны и протестированы клиентская и серверная части приложения,
обеспечивающие взаимодействие для выполнения математической операции на основе теоремы Пифагора.