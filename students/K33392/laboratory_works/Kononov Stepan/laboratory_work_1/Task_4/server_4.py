import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5555))
server_socket.listen(5)

clients = {}
addresses = {}


def broadcast(message, sender_name):
    for client, client_name in clients.items():
        if client_name != sender_name:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)


def remove(client):
    if client in clients:
        client_name = clients[client]
        del clients[client]
        del addresses[client]
        print(f"{client_name} покинул чат")
        broadcast(f"{client_name} покинул чат", None)


def handle_client(client):
    try:
        client_name = client.recv(1024).decode('utf-8')
        clients[client] = client_name
        addresses[client] = client.getpeername()
        print(f"{client_name} присоединился к чату")
        broadcast(f"{client_name} присоединился к чату", None)
    except:
        return

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            if message.startswith("@"):
                recipient, message = message.split(" ", 1)
                recipient = recipient[1:]
                if recipient in clients.values():
                    recipient_socket = [client for client, name in clients.items() if name == recipient][0]
                    recipient_socket.send(f"{clients[client]} (личное сообщение): {message}".encode('utf-8'))
            else:
                print(f"{clients[client]}: {message}")
                broadcast(f"{clients[client]}: {message}", clients[client])
        except:
            remove(client)

    remove(client)


while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключено: {client_address}")

    client_thread = threading.Thread(target=lambda: handle_client(client_socket))
    client_thread.start()
