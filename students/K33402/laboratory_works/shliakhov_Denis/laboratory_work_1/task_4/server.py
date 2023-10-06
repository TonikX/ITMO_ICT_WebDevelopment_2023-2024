import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9090))
server.listen(5)

clients = []
nicknames = []


def send_message(message, nickname):
    mess = f"{nickname}: {message}".encode()
    for client in clients:
        client.send(mess)


def handle_client(client):
    index = clients.index(client)
    nickname = nicknames[index]
    while True:
        try:
            message = client.recv(1024).decode()
            send_message(message, nickname)
        except:
            clients.remove(client)
            client.close()
            send_message("Вышел из чата", nickname)
            nicknames.remove(nickname)
            break


while True:
    client_socket, addr = server.accept()
    client_socket.send("nickname".encode())
    nickname = client_socket.recv(1024).decode()
    nicknames.append(nickname)
    clients.append(client_socket)
    send_message("Вошел в чат", nickname)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
