# Задание 4: Реализация двухпользовательского или многопользовательского чата


## Описание задания

В данном задании требуется создать чат, который может поддерживать двухпользовательский или многопользовательский режим. Реализация многопользовательского чата позволяет получить максимальное количество баллов.

Чат можно реализовать с использованием протокола TCP (Transmission Control Protocol) для 100% баллов или с использованием протокола UDP (User Datagram Protocol) для 80% баллов.

Для реализации многопользовательского чата необходимо использовать библиотеку `threading`, чтобы создать отдельные потоки для обработки сообщений от каждого пользователя.

## Клиентская часть

### 1. Отправка сообщений

Клиентская часть должна предоставлять возможность пользователю отправлять сообщения в чат. Это можно сделать, считывая ввод с клавиатуры и отправляя сообщение на сервер через сокет.

### 2. Прием сообщений

Клиент также должен быть способен получать сообщения от других пользователей и отображать их на экране. Это также можно реализовать в отдельном потоке, который постоянно ожидает приходящих сообщений от сервера.

## Серверная часть

### 1. Создание сервера и подключение клиентов

Сервер должен создать сокет и привязать его к определенному адресу и порту. Затем сервер должен ожидать подключения клиентов и принимать их.

### 2. Регистрация и имена пользователей

Каждый клиент, подключающийся к серверу, должен выбирать себе уникальное имя пользователя. Это имя будет использоваться для идентификации отправителя сообщения. После регистрации имени, сервер должен сохранять связь между сокетами и именами пользователей.

### 3. Прием и рассылка сообщений

Сервер должен ожидать сообщения от клиентов и рассылать их другим подключенным клиентам. Сервер должен обрабатывать и отправлять сообщения в отдельных потоках для каждого клиента. Когда сервер получает сообщение от одного клиента, он должен отправить его всем остальным клиентам.

### 4. Завершение работы клиента

Когда клиент отключается от чата, сервер должен удалить его из списка активных клиентов и сообщить об этом остальным пользователям.

## Примеры кода

Приведены примеры кода для клиентской и серверной частей чата в языке Python, использующего протокол TCP.

```python
# Пример клиентской части

import socket
import threading

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8878))
username = input("Введите ваше имя: ")
client.send(username.encode('utf-8'))
send_thread = threading.Thread(target=send_messages, args=(client,))
receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread.start()
receive_thread.start()
```

```python
# Пример серверной части

import socket
import threading

clients = {}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8878))
server.listen(5)

def handle_client(client_socket, username):
    while True:
        try:
            if message := client_socket.recv(1024).decode('utf-8'):
                print(f"{username}: {message}")
                broadcast(message, username)
            else:
                remove_client(client_socket, username)
                break
        except Exception as e:
            print(e)
            remove_client(client_socket, username)
            break

def broadcast(message, username):
    for client in clients:
        if clients[client] != username:
            client.send(f"{username}: {message}".encode('utf-8'))

def remove_client(client_socket, username):
    del clients[client_socket]
    broadcast(f"{username} покинул чат.", "Сервер")
    client_socket.close()

while True:
    client_socket, addr = server.accept()
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"Присоединился {username} ({addr[0]}:{addr[1]})")
    broadcast(f"{username} присоединился к чату.", "Сервер