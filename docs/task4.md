# Упражнение 4

## Описание Задачи

Цель задания - Реализовать двух пользовательский или многопользовательский чат.


## Реализация

### Сервера
Код файла `main.py`
```python
from threading import Thread

if __name__ == '__main__':
    server = create_server()
    laddr = server.getsockname()
    print('running on ', laddr)
    port = laddr[1]

    threads = []
    while True:
        # establish connection with client
        conn, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])

        data = conn.recv(1024)
        name = data.decode('utf-8')
        if name in clients.values():
            data = f"'{name}' уже тут, вы не '{name}'".encode('utf-8')
            conn.send(data)
            conn.close()
            continue

        for _, friend in clients.items():
            data = f"server: пришел '{name}'".encode('utf-8')
            friend.send(data)

        with lock:
            clients[name] = conn

        t = Thread(target=threaded, args=(conn, name, ))
        t.start()
        threads.append(t)
```
Создаётся сервер и выводится ip-адрес и порт. Затем в цикле устанавливаются подключенные пользователи и происходит отправка сообщений о подключении
### Клиента

Клиент имеет 2 потока. Один для ввода сообщений. Другой для вывода сообщений
```python
import socket
import time
from multiprocessing import Process
from typing import Tuple

def split_text(text: str) -> Tuple:
    parts = text.split(':')
    if len(parts) != 2:
        print("ошибка! формат 'имя: сообщение'")
        return None, None,

    f_name = parts[0]
    message = parts[1].lstrip()
    return f_name, message,


def receive(conn: socket):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 61021
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    name = "John"  # name
    s.send(name.encode('utf-8'))

    t_receive = Process(target=receive, args=(s, ))
    t_receive.start()

    while True:
        # ask the client whether he wants to continue
        text = input(':')

        if text == 'q':
            break

        friend_name, _ = split_text(text)
        if friend_name is None:
            continue

        if friend_name != name and t_receive.is_alive():
            s.send(text.encode('utf-8'))
            # print(f"{name}->{text}")
        else:
            continue

    if t_receive.is_alive():
        t_receive.terminate()

    s.close()
```
В main клиента задаётся адрес и хост, а также автоматически присваивается имя. Затем идёт обработка возможных сообщений и проверка наличия собеседника.


### Функции сервера

```python
import socket
import sys
import time
from threading import Lock
from typing import List, Dict

def create_server() -> socket:
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 0,))
        server.listen(4)
    except OSError as msg:
        print(msg)
        sys.exit(1)

    if server is None:
        print('could not open server socket')
        sys.exit(1)

    return server


def run_server_connection(server: socket, clients: Dict, lock: Lock) -> None:
    conn, _ = server.accept()
    with (conn):
        data = conn.recv(1024)
        name = data.decode('utf-8')
        if name in clients.values():
            data = f"'{name}' уже тут, вы не '{name}'".encode('utf-8')
            conn.send(data)
            return

        for _, friend in clients.items():
            data = f"server: пришел '{name}'".encode('utf-8')
            friend.send(data)

        with lock:
            clients[name] = conn


def loop(clients: Dict, lock: Lock):
    while True:
        for name, conn in clients.items():
            print('loop', name)
            # data = f"server: пришел '{name}'".encode('utf-8')
            # friend.send(data)
            pass
        time.sleep(1)
```
В этой части кода создаётся сервер, происходят этапы подключения пользователей и проверки. По окончанию выводится сообщение о новом пользователе.

### Клиент №2

Клиент также имеет 2 потока. Один для ввода сообщений. Другой для вывода сообщений
```python
import socket
import time
from multiprocessing import Process
from typing import Tuple

def split_text(text: str) -> Tuple:
    parts = text.split(':')
    if len(parts) != 2:
        print("ошибка! формат 'имя: сообщение'")
        return None, None,

    f_name = parts[0]
    message = parts[1].lstrip()
    return f_name, message,


def receive(conn: socket):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 61021
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    name = "Mark"  # name
    s.send(name.encode('utf-8'))

    t_receive = Process(target=receive, args=(s, ))
    t_receive.start()

    while True:
        # ask the client whether he wants to continue
        text = input(':')

        if text == 'q':
            break

        friend_name, _ = split_text(text)
        if friend_name is None:
            continue

        if friend_name != name and t_receive.is_alive():
            s.send(text.encode('utf-8'))
            # print(f"{name}->{text}")
        else:
            continue

    if t_receive.is_alive():
        t_receive.terminate()

    s.close()
```
Здесь другое имя пользователя, но логика схожая с первым пользователем.
