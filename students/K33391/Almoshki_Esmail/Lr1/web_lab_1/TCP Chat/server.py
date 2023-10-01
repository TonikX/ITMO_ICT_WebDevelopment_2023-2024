import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEAD = 1024
FORMAT = 'utf-8'
ADDRESS = (SERVER, PORT)

clients = []
nicknames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def start_server():
    print(f'[LAUNCHING] server is listening on {SERVER}')
    server.listen()
    while True:
        conn, add = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, add))
        thread.start()


def handle_client(conn, add):
    while True:
        conn.send("NICKNAME".encode(FORMAT))
        nickname = conn.recv(HEAD).decode(FORMAT)
        print(f'{nickname} joined the chat')
        if nickname:
            nicknames.append(nickname)
            clients.append(conn)
            conn.send("MASSAGE".encode(FORMAT))
            massage = nickname + " : " + conn.recv(HEAD).decode(FORMAT)
            send_live(massage)


def send_live(massage):
    for client in clients:
        client.send(massage.encode(FORMAT))


start_server()
