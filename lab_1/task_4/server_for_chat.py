import socket
import threading

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'

clients = []


def sharing_message(message):
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            sharing_message(message)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(15)

    print(f"Server listening on {IP}:{PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
