import socket
import threading

# Создаем TCP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Список клиентов и их соединений
clients = []
client_lock = threading.Lock()

def broadcast_message(message, sender):
    with client_lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(message.encode())
                except:
                    # Если отправка сообщения не удалась, удаляем клиента из списка
                    remove_client(client)

def remove_client(client):
    with client_lock:
        if client in clients:
            clients.remove(client)

def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            broadcast_message(message, client_socket)
        except:
            pass  # Обработка ошибок

    # Удаляем клиента из списка и закрываем соединение
    remove_client(client_socket)
    client_socket.close()

server_socket.listen(5)
print("Сервер чата запущен. Ожидание подключения клиентов...")

while True:
    client_connection, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")

    with client_lock:
        clients.append(client_connection)

    # Создаем отдельный поток для обработки клиента
    client_thread = threading.Thread(target=client_handler, args=(client_connection,))
    client_thread.start()