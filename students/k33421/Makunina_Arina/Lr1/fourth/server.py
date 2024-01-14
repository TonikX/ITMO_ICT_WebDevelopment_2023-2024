import socket
import threading

clients = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8878))
server.listen(5)


# Функция для обработки сообщений от клиентов
def handle_client(client_socket, username):
    while True:
        try:
            if message := client_socket.recv(1024).decode('utf-8'):
                print(f"{username}: {message}")
                broadcast(message, username)
            else:
                remove_client(client_socket, username)
                break
        except Exception as e:
            print(e)
            remove_client(client_socket, username)
            break


# Функция для отправки сообщения всем клиентам
def broadcast(message, username):
    for client in clients:
        if clients[client] != username:
            client.send(f"{username}: {message}".encode('utf-8'))


# Функция для удаления клиента из списка
def remove_client(client_socket, username):
    del clients[client_socket]
    broadcast(f"{username} покинул чат.", "Сервер")
    client_socket.close()


# Основной цикл сервера
while True:
    client_socket, addr = server.accept()
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"Присоединился {username} ({addr[0]}:{addr[1]})")
    broadcast(f"{username} присоединился к чату.", "Сервер")
    client_socket.send("Вы присоединились к чату.".encode('utf-8'))

    # Запускаем поток для обработки клиента
    client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
    client_handler.start()
