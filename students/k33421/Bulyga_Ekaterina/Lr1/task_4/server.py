import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


# Отправка сообщения всем пользователям
def broadcast(message):
    for client in clients:
        client.send(message)


# Обработка сообщений от пользователей
def handle(client):
    while True:
        try:
            # Отправка сообщений
            message = client.recv(1024)
            broadcast(message)
        except:
            # Завершение работы пользователя
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left!'.encode('ascii'))
            nicknames.remove(nickname)
            break


while True:
    # Соединение
    client, address = server.accept()
    print(f"Connected with {address}")

    # Запрос и сохранение никнейма
    client.send('NICK'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)

    # Рассылка сообщения о присоединении пользователя
    print(f"Nickname is {nickname}")
    broadcast(f"{nickname} joined!".encode('ascii'))
    client.send('Connected to server!'.encode('ascii'))

    # Запуск обработчика сообщений (потока) пользователя
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
