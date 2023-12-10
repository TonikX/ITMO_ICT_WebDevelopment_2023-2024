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
