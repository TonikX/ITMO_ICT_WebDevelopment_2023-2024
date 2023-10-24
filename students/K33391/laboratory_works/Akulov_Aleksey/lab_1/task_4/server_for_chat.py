import socket
import threading

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'

clients = []
client_names = {}


def elim_client(client_socket):
    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)
    if client_socket in client_names:
        del client_names[client_socket]


def sharing_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                elim_client(client)



def handle_client(client_socket):
    name = client_socket.recv(1024).decode(codage)
    client_names[client_socket] = name

    print(f"{name} has joined the chat!")
    welcome_msg = f"{name} has joined the chat!".encode(codage)
    sharing_message(welcome_msg, client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            formatted_message = f"{name}: {message.decode(codage)}".encode(
                codage)
            sharing_message(formatted_message, client_socket)
        except:
            print(f"{name} has left the chat!")
            leave_msg = f"{name} has left the chat!".encode(codage)
            sharing_message(leave_msg, None)

            elim_client(client_socket)
            break


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(15)

    print(f"Server listening on {IP}:{PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client,
                                         args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
