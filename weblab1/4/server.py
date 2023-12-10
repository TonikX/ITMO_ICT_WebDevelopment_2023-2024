import socket
import threading


def send_message(msg, client_address):
    msg = f"{client_address}: " + msg

    for client in clients:
        if client == client_address:
            continue
        client.send(msg.encode())


def client_work(connection, address):
    while True:
        msg = connection.recv(128).decode()
        if (msg is None) or (msg == 'exit'):
            break
        send_message(msg, address)

    connection.close()


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 55555))
socket.listen()

clients = list()
while True:
    connection, address = socket.accept()
    send_message('New user', connection)
    clients.append(connection)

    client_thread = threading.Thread(target=client_work, args=(connection, address))
    client_thread.start()
    print('pup')
