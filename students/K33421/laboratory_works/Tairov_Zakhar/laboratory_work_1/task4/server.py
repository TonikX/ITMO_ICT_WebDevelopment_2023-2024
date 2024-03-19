import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

CLIENTS = {}

def client_handler(client_sock):
    name = client_sock.recv(1024).decode()
    CLIENTS[name] = client_sock
    while True:
        try:
            msg = client_sock.recv(1024).decode()
            print(f"{name}: {msg}")
            if not msg:
                break
            for client in CLIENTS.keys():
                if client != name:
                    CLIENTS[client].send(f"{name}: {msg}".encode())
        except ConnectionResetError:
            break

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        while True:
            client_sock, _ = sock.accept()
            threading.Thread(target=client_handler, args=(client_sock,)).start()
except KeyboardInterrupt:
    exit()