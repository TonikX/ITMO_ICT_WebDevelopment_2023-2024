import socket
import threading

PORT = 8080
clients = {}


def chat(client_socket):
    global clients

    while True:
        mail = client_socket.recv(1024).decode('utf-8')
        for sock in clients.keys():
            sock.send(f'{clients[client_socket]} send: {mail}'.encode('utf-8'))


def main():

    global PORT
    global clients

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    while True:
        client_socket, (client_host, client_port) = server_socket.accept()
        client_socket.send(b'Enter your nickname: ')
        nick = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = nick
        thread = threading.Thread(target=chat, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    main()