# Практическое задание 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.
Обязательно использовать библиотеку

Реализовать с помощью протокола TCP – 100% баллов, с помощью UDP – 80%.

Обязательно использовать библиотеку threading.

Для реализации с помощью UDP, thearding использовать для получения
сообщений у клиента.

Для применения с TCP необходимо запускать клиентские подключения И прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.

### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading
    
PORT = 8080
clients = {}
```

###### Тело сервера

```
def main():

    global PORT
    global clients

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    while True:
        client_socket, (client_host, client_port) = server_socket.accept()
        client_socket.send(b'Enter your nickname: ')
        nick = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = nick
        thread = threading.Thread(target=chat, args=(client_socket,))
        thread.start()
```

###### Обработка сообщений от клиентов
```
def chat(client_socket):
    global clients

    while True:
        mail = client_socket.recv(1024).decode('utf-8')
        for sock in clients.keys():
            sock.send(f'{clients[client_socket]} send: {mail}'.encode('utf-8'))

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

    global PORT

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))
    message = client_socket.recv(4096)
    print(message.decode())
    nick = input()
    client_socket.send(nick.encode('utf-8'))
    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()
```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
```
