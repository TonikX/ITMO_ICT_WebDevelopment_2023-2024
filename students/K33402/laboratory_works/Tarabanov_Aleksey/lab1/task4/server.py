import socket
import threading

clients = {}
last_messages = {}

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            if check_spam(username, message):
                pass
            else:
                send_to_all(username + ": " + message, client_socket)
                print(username + ": " + message)

        except Exception as e:
            print(f"Ошибка при обработке сообщения от {username}: {e}")
            break

    #Кикаем
    del clients[username]
    del last_messages[username]
    print(f"{username} отключен")
    send_to_all(f"{username} покинул чат", client_socket)
    client_socket.close()


def send_to_all(message, sender_socket):
    for client, socket in clients.items():
        if socket != sender_socket:
            try:
                socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Ошибка при отправке сообщения клиенту {client}: {e}")


def check_spam(username, message):
    if username in last_messages and last_messages[username] == message:
        if username in clients:
            clients[username].sendall("Спам предупреждение: Не отправляйте одинаковые сообщения!".encode('utf-8'))
            return True
        else:
            return False
    else:
        return False
    last_messages[username] = message


HOST = 'localhost'
PORT = 2210

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер слушает на {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"{username} присоединился к чату")
        send_to_all(f"{username} присоединился к чату", client_socket)

        # Запуск потока для обработки сообщений от клиента
        threading.Thread(target=handle_client, args=(client_socket, username)).start()
