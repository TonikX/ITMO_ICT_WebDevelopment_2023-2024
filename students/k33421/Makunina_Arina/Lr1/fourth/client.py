import socket
import threading


# Функция для отправки сообщений
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


# Функция для приема сообщений от сервера
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)


# Создаем клиентский сокет
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8878))

# Регистрация по имени
username = input("Введите ваше имя: ")
client.send(username.encode('utf-8'))

# Запускаем потоки для отправки и приема сообщений
send_thread = threading.Thread(target=send_messages, args=(client,))
receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread.start()
receive_thread.start()
