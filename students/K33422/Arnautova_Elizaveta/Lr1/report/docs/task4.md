**Задание:** 4.	Реализовать двухпользовательский или многопользовательский чат. Реализация многопользовательского часа позволяет получить максимальное количество баллов.

Обязательно использовать библиотеку *threading*. 

Реализовать с помощью протокола TCP – 100% баллов, с помощью UDP – 80%.

- Для реализации с помощью UDP, thearding использовать для получения сообщений у клиента.
- Для применения с TCP необходимо запускать клиентские подключения И прием и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров, чтобы потом отправлять им сообщения. 


**Код сервера:**
```python
import socket
import threading

HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, SERVER_PORT))
server.listen()

clients = []
names = []


def broadcast(message, sender):  # рассылка сообщения всем клиентам из списка клиентов
    for client in clients:
        if sender != client:
            client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(BUFF_SIZE)
            broadcast(message, client)

        except:  # если пользователь от нас сбежал
            name = names[clients.index(client)]
            clients.remove(client)
            names.remove(name)
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('name'.encode('utf-8'))  # запрос имени пользователя
        name = client.recv(BUFF_SIZE).decode('utf-8')
        names.append(name)
        clients.append(client)

        print("Name is {}".format(name))
        broadcast("{} joined!".format(name).encode('utf-8'), client)
        client.send('You are connected!\nTo terminate the connection to the server, enter leave'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()

```

**Код клиента:**
```python
import socket
import threading
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

name = input("What is your name? ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))


def input_information():
    while True:
        try:
            message = client.recv(BUFF_SIZE).decode('utf-8')
            if message == 'name':
                client.send(name.encode('utf-8'))
            else:
                print(message)

        except:
            client.close()
            break


def output_information():
    while True:
        message = input('')
        if message == 'leave':
            client.send(f'*{name} left*'.encode('utf-8'))
            client.close()
            break

        message = '{}: {}'.format(name, message)
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=input_information)
receive_thread.start()

write_thread = threading.Thread(target=output_information)
write_thread.start()

```

**Скринкаст:**

Клиент-серверное взаимодействие:

На стороне клиентов:
![](/screenshots/4-client1.png)

![](/screenshots/4-client2.png)
Демонстрируется, когда кто-то подключился и сообщения с именем. Если пользователь отключается, используя команду, остальным приходит уведомление об этом.

На стороне сервера:
![](/screenshots/4-server.png)