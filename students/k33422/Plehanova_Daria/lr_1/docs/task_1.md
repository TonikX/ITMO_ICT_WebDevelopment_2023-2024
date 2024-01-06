# Задание 1

## Описание Задачи

Цель задания - реализовать простое клиент-серверное приложение с использованием сокетов и протокола UDP. Клиент
отправляет сообщение "Hello, server" на сервер, который, в свою очередь, отвечает сообщением "Hello, client". Важно
обеспечить корректную передачу сообщений и их отображение на обеих сторонах.

## Реализация

### Серверная Часть

Файл: `server.py`

Сервер прослушивает входящие UDP-сообщения и отправляет ответ. Сервер ожидает сообщения от клиента, выводит его
содержимое в консоль, а затем отправляет обратно клиенту сообщение "Hello, client!".

```python
import socket

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        
        while True:
            data, addr = conn.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            conn.sendto(b"Hello, client!", addr)
```

### Клиентская Часть

Файл: `client.py`

Клиент отправляет сообщение "Hello, server!" на сервер и ожидает ответа. После получения ответа от сервера, содержимое
сообщения выводится в консоль.

```python
import socket

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:
        conn.sendto(b"Hello, server!", ('127.0.0.1', 8888))
        data, addr = conn.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
```

## Выводы

Реализовано клиент-серверное взаимодействие с использованием библиотеки `socket` и протокола
UDP. Тестирование показало корректную работу обеих частей приложения.