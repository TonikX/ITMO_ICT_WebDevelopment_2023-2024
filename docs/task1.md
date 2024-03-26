# Упражнение 1

## Описание Задачи

Цель задания - Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

## Код 

### Клиента

```python
import socket
import sys

def run_udp_client(port: int, buffer_size: int) -> None:
    HOST = None                 # Symbolic name meaning all available interfaces
    client = None

    for res in socket.getaddrinfo(HOST, port, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP, socket.AI_PASSIVE):
        af, sock_type, proto, canonname, sa = res
        try:
            client = socket.socket(af, sock_type, proto)

            bytes_to_send = "Hello UDP Server".encode()
            client.sendto(bytes_to_send, sa)

            bytes_from_server = client.recvfrom(buffer_size)
            message = bytes_from_server[0].decode()
            print(f"Message from Server: {message}")
            break

        except OSError as msg:
            print(msg)
            sys.exit(1)

    if client is None:
        print('could not open client socket')
        sys.exit(1)
```

Во фрагменте представленного кода функция `run_udp_client` создает UDP клиента, который отправляет сообщение "Hello UDP Server" на выбранный порт.

### Сервера

```python
import socket
import sys

def run_udp_server(port: int, buffer_size: int) -> None:
    HOST = None                 # Symbolic name meaning all available interfaces
    server = None

    for res in socket.getaddrinfo(HOST, port, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP, socket.AI_PASSIVE):
        af, sock_type, proto, canonname, sa = res
        try:
            server = socket.socket(af, sock_type, proto)
            server.bind(sa)
            break
        except OSError as msg:
            print(msg)
            sys.exit(1)

    if server is None:
        print('could not open server socket')
        sys.exit(1)

    while True:
        bytes_and_address = server.recvfrom(buffer_size)
        message = bytes_and_address[0]
        address = bytes_and_address[1]
        print(f"Message from Client: {message.decode()}")

        # Sending a reply to client
        bytes_to_send = "Hello UDP Client".encode()
        server.sendto(bytes_to_send, address)
```
Сервер прослушивает входящие UDP-сообщения и отправляет ответ.