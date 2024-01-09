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
SERVER_PORT = 14901
BUFF_SIZE = 16384

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, SERVER_PORT))
server.listen()

clients = []
names = []


def broadcast(message, sender):  # рассылает сообщение всем клиентам, кроме отправителя:
    for client in clients:
        if sender != client:
            client.send(message)


def handle(client):  # обрабатывает соединение с клиентом
    while True:  # ожидает получение сообщения от клиента.
        try:  # Если получено сообщение, вызывается функция broadcast для рассылки сообщения всем клиентам.
            message = client.recv(BUFF_SIZE)
            broadcast(message, client)

        except:  # Если возникает ошибка (например, клиент отключается), происходит удаление клиента из списков
            # clients и names, закрытие соединения с клиентом и выход из цикла.
            name = names[clients.index(client)]
            clients.remove(client)
            names.remove(name)
            client.close()
            break


def receive():  # принимает входящие соединения от клиентов
    while True:  # ожидает подключения клиентов к серверу
        client, address = server.accept()
        print("Connected with {}".format(str(address)))  # При подключении клиента, выводится сообщение о подключении

        client.send('name'.encode('utf-8'))  # отправляется запрос имени пользователя.
        name = client.recv(BUFF_SIZE).decode('utf-8')
        names.append(name)  # имя добавляется в список names
        clients.append(client)  # сокет клиента добавляется в список clients.

        # Отправляется сообщение всем клиентам о присоединении нового пользователя.
        print("Name is {}".format(name))
        broadcast("{} joined!".format(name).encode('utf-8'), client)

        # Клиенту отправляется приветственное сообщение и инструкция по завершению соединения.
        client.send('You are connected!\nTo terminate the connection to the server, enter leave'.encode('utf-8'))

        # Запускается новый поток, в котором вызывается функция handle для обработки соединения с клиентом
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()


```

**Код клиента:**
```python
import socket
import threading

HOST = '127.0.0.1'
SERVER_PORT = 14901
BUFF_SIZE = 16384

name = input("What is your name? ")  # запрос имени пользователя
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание TCP сокета клиента
client.connect((HOST, SERVER_PORT))  # подключение клиента к указанному хосту и порту


def input_information():  # обрабатывает входящую информацию от сервера
    while True:  # ожидает получение сообщения от сервера
        try:
            message = client.recv(BUFF_SIZE).decode('utf-8')
            if message == 'name':  # Если получено сообщение 'name', клиент отправляет свое имя на сервер
                client.send(name.encode('utf-8'))
            else:  # В противном случае, сообщение выводится в консоль
                print(message)

        except:
            client.close()
            break


def output_information():  # обрабатывает исходящую информацию от клиента
    while True:
        message = input('')  # ожидает ввод сообщения от пользователя
        if message == 'leave':                              # Если введено сообщение 'leave',
            client.send(f'*{name} left*'.encode('utf-8'))   # клиент отправляет сообщение о своем уходе на сервер
            client.close()                                  # и закрывает соединение
            break

        message = '{}: {}'.format(name, message)    # иначе сообщение форматируется как "{имя}: {сообщение}"
        client.send(message.encode('utf-8'))        # и отправляется на сервер


receive_thread = threading.Thread(target=input_information)  # создание потока для функции input_information
receive_thread.start()

write_thread = threading.Thread(target=output_information)  # создание потока для функции output_information
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