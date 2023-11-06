import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except OSError:
            break

def send_message(client_socket, username):
    while True:
        message = input()
        full_message = f"{username}: {message}"
        client_socket.send(full_message.encode())

def start_client():
    host = 'localhost'
    port = 9999

    username = input("Введите ваше имя: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Отправляем имя пользователя серверу
    client_socket.send(username.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client_socket, username))
    send_thread.start()

start_client()