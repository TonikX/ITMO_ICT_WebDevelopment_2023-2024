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
