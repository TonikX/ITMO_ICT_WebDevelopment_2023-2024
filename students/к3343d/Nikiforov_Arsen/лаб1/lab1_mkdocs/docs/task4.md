## Задание №4

---
**Задача:**

Реализовать двухпользовательский или многопользовательский чат. Реализация многопользовательского часа позволяет получить максимальное количество баллов.

Обязательно использовать библиотеку 

Полезные ссылки:

- [https://docs.python.org/3/library/threading.html](https://docs.python.org/3/library/threading.html)
- [https://webdevblog.ru/vvedenie-v-potoki-v-python/](https://webdevblog.ru/vvedenie-v-potoki-v-python/)

**Требования:**

- Реализовать с помощью протокола TCP.
- Обязательно использовать библиотеку threading. 
- Для реализации с помощью UDP, thearding использовать для получения сообщений у клиента.
- Для применения с TCP необходимо запускать клиентские подключения *И* прием и отправку сообщений всем юзерам на сервере в потоках. 
- Не забудьте сохранять юзеров, чтобы потом отправлять им сообщения. 

---
## Решение

**client.py**
```python
import socket
import threading

class Client:
    def __init__(self, host='127.0.0.1', port=55555):
        self.nickname = input("Введите ваш никнейм: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("Произошла ошибка!")
                self.client.close()
                break

    def write(self):
        while True:
            message = input("")
            if message.lower() == 'quit':  # Проверка на команду "quit" для выхода
                self.client.send('quit'.encode('utf-8'))
                break
            else:
                message_to_send = f'{self.nickname}: {message}'
                self.client.send(message_to_send.encode('utf-8'))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

client = Client()
client.run()
```

**server.py**
```python
import threading
import socket

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []       # Список подключенных клиентов
        self.nicknames = []     # Список никнеймов клиентов

    def broadcast(self, message):
        # Рассылка сообщения всем клиентам
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)  # Прием сообщения от клиента (максимум 1024 байта)
                self.broadcast(message)     # Рассылка сообщения всем клиентам
            except:
                # Обработка исключений, если клиент отключился
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat!'.encode('ascii'))
                break
            
    def receive(self):
        while True:
            client, address = self.server.accept()  # Принятие нового клиента и его адреса
            print(f'Connected with {str(address)}')

            client.send('NICK'.encode('ascii'))     # Запрос никнейма у клиента
            nickname = client.recv(1024).decode('ascii')  # Получение никнейма от клиента
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}!')
            self.broadcast(f'{nickname} joined the chat!'.encode('ascii'))  # Оповещение о входе клиента
            client.send('Connected to the server!'.encode('ascii'))  # Отправка клиенту сообщения о подключении

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()  # Запуск обработки сообщений клиента в отдельном потоке

    def run(self):
        print("Server started...")
        self.receive()  # Запуск прослушивания подключений и обработки клиентов

server = Server()
server.run()
```
**Что делает код:**

- Клиент и сервер обмениваются сообщениями через сокеты. Клиенты могут отправлять сообщения на сервер и принимать сообщения от других клиентов через многопоточность. Сервер принимает новых клиентов, сохраняет их данные и рассылает сообщения между клиентами.

---
##Результат работы программы

**client.py:**

- Импорт библиотек: socket (работа с сетью), threading (многопоточность).
- Создание класса Client для клиента.
- В конструкторе клиента устанавливается соединение с сервером, запрашивается никнейм.
- receive - метод для получения сообщений от сервера.
- write - метод для отправки сообщений на сервер.
- run - метод для запуска потоков получения и отправки сообщений.

![задание №4](img/4_1.jpg)


**Страница отображения оценок (server.py):**

- Импорт библиотек: threading (многопоточность), socket (работа с сетью).
- Создание класса Server для сервера.
- В конструкторе сервера настраивается прослушивание порта и создаются списки клиентов и их никнеймов.
- broadcast - метод для рассылки сообщений всем клиентам.
- handle - метод для обработки сообщений от клиента.
- receive - метод для принятия новых клиентов и запуска потоков обработки сообщений.

![задание №4](img/4_2.png)