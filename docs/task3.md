# Упражнение 3

## Описание Задачи

Цель задания - Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла `index.html` .

## Код

### Клиента
```python
import socket
import sys
import time

def run_tcp_client(port: int, buffer_size: int) -> None:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', port, ))
    except OSError as msg:
        print(msg)
        sys.exit(1)

    if client is None:
        print('could not open client socket')
        sys.exit(1)

    with client:
        data = client.recv(buffer_size)
        print("Client:\n", data.decode('utf-8'))
        time.sleep(3.0)
        # get html again
        hi = 'hi'.encode('utf-8')
        client.sendall(hi)
        data = client.recv(buffer_size)
        print("Client:\nx2\n" + data.decode('utf-8'))
        time.sleep(1.0)
        # stop it
        stop = 'stop'.encode('utf-8')
        client.sendall(stop)
```

### Сервер 
```python
import socket
import sys

def create_server() -> socket:
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 0, ))
        server.listen(1)
    except OSError as msg:
        print(msg)
        sys.exit(1)

    if server is None:
        print('could not open server socket')
        sys.exit(1)

    return server


def run_server_connection(server: socket) -> None:
    print('Server: Wait...')
    conn, addr = server.accept()
    with conn:
        print('Server: Connected by', addr)
        file = open("hello.html", "r")
        hello = file.read()
        data = hello.encode('utf-8')
        conn.send(data)
        while True:
            r = conn.recv(1024)
            if r.decode('utf-8') == 'stop':
                break
            else:
                print("Server:", r.decode('utf-8'))
                conn.send(data)
```

Сервер использует протокол TCP для прослушивания подключений клиентов. При подключении клиента сервер загружает HTML-страницу из файла `hello.html` и отправляет её клиенту в виде HTTP-ответа.

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>3-socket</title>
</head>
<body>
    <p>
        Today is a beautiful day. We go swimming and fishing.
    </p>
</body>
</html>
```