# Multiprocessing - Server side

import socket
from threading import Thread


#   рассылка сообщений всем клиентам
def send_all(msg):
    global clients
    for client in clients:
        client.send(msg.encode("utf-8"))


#   обработка сообщений одного клиента
def handle(client):
    global clients
    while True:
        try:
            data = client.recv(2048)
            if not data:
                raise Exception
            message = clients[client] + ': ' + data.decode("utf-8")
            send_all(message)
            print(message)
        except:
            name = clients[client]
            del clients[client]
            client.close()
            send_all(f"{name} has left the chat")
            print(f"{name} disconnected")
            break


#   первичное соединение с клиентом
def connect():
    global clients
    while True:
        client, address = sock.accept()
        print(f"Connected to a client at {address}")

        client.send(b'nickname')
        data = client.recv(2048)
        name = data.decode('utf-8')
        clients[client] = name
        print(f"Client at {address} has set a nickname: {name}")
        send_all(f"{name} has joined the chat")
        th = Thread(target=handle, args=(client,))
        th.start()


clients = dict()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 20000))
sock.listen()

print("Chat server\nWaiting for users...")
connect()

