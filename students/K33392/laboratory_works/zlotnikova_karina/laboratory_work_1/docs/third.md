# Практическое задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

**Полезные ссылки:**

- http://zetcode.com/python/socket/

Обязательно использовать библиотеку socket

### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело сервера

```
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=(client_socket, ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break
```

###### Обработка подключения

```
def chat(client_socket):
    while True:
        client_socket.recv(1000)
        response_type = 'HTTP/1.0 200 OK\n'
        headers = 'Content-Type: text/html\n\n'
        with open('index.html', 'r') as f:
            body = f.read()

        response = response_type + headers + body
        client_socket.send(response.encode('utf-8'))
```

### Клиент

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело клиента

```
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()

```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        client_socket.send(b"GET / HTTP/1.0\r\nHost:localhost\r\n\r\n")
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
```
