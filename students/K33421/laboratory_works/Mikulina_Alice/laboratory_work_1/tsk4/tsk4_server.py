import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

server_socket.bind(server_address)

server_socket.listen(5)
print("Server is running on {}:{}".format(*server_address))

clients = []

def handle_client(client_socket, client_address):
    client_name = client_socket.recv(1024).decode()
    print("New connection from {}: {} joined".format(client_address[0], client_name))

    clients.append((client_socket, client_name))

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            for client in clients:
                if client[0] != client_socket:
                    client[0].send("{}: {}".format(client_name, message).encode())
        except ConnectionResetError:
            break

    clients.remove((client_socket, client_name))
    print("Connection closed from {}: {}".format(client_address[0], client_name))

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()