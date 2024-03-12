import socket  # Импортируем модуль socket для сетевого программирования
import threading  # Импортируем модуль threading для многопоточности

# Создаем сокет сервера, используя IPv4 и TCP протокол
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9991))  # Привязываем сервер к локальному адресу и порту 9991
server.listen()  # Сервер начинает принимать подключения

clients = []  # Список для хранения подключенных клиентов
nicknames = []  # Список для хранения никнеймов клиентов


def broadcast(message):  # Функция для отправки сообщений всем клиентам
    for client in clients:
        client.send(message)


def handle(client):  # Функция для обработки сообщений от клиентов
    while True:
        try:
            message = client.recv(1024)  # Принимаем сообщение от клиента
            broadcast(message)  # Отправляем сообщение всем клиентам
        except:
            index = clients.index(client)  # Находим индекс клиента, который прервал соединение
            clients.remove(client)  # Удаляем клиента из списка
            client.close()  # Закрываем соединение с клиентом
            nickname = nicknames[index]  # Получаем никнейм клиента
            broadcast(f'{nickname} left the chat.'.encode('utf-8'))  # Оповещаем всех о выходе клиента из чата
            nicknames.remove(nickname)  # Удаляем никнейм из списка
            break  # Выходим из цикла


def receive():  # Функция для принятия новых подключений
    while True:
        client, address = server.accept()  # Принимаем подключение от клиента
        client.send('Nick'.encode('utf-8'))  # Запрашиваем у клиента никнейм
        nickname = client.recv(1024).decode('utf-8')  # Принимаем никнейм клиента
        nicknames.append(nickname)  # Добавляем никнейм в список
        clients.append(client)  # Добавляем клиента в список

        print(f'Nickname of the client is: {nickname}')  # Выводим никнейм подключившегося клиента
        broadcast(f'{nickname} joined the chat.'.encode('utf-8'))  # Оповещаем всех о подключении нового клиента
        client.send('Connected to the server'.encode('utf-8'))  # Отправляем клиенту сообщение о подключении к серверу

        thread = threading.Thread(target=handle, args=(client,))  # Создаем отдельный поток для клиента
        thread.start()  # Запускаем поток


print('Server is listening...')  # Выводим сообщение о начале работы сервера
receive()  # Запускаем функцию для принятия подключений
