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
