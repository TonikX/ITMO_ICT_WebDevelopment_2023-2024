import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1"
server_port = 80
server_socket.bind((server_host, server_port))
server_socket.listen(5)

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                remove_client(client_socket)
                break
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Ошибка при обработке сообщения: {e}")
            remove_client(client_socket)
            break


def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
                client.close()
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Подключено клиентов: {client_address[0]}:{client_address[1]}")
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
