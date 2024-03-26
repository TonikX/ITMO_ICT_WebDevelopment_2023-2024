import socket
import threading


# Функция для чтения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            # Получение сообщения от сервера
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Ошибка при получении сообщения от сервера: {e}")
            break


HOST = '45.138.26.182'
PORT = 2210

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    username = input("Введите ваше имя: ")
    client_socket.sendall(username.encode('utf-8'))

    # Запуск потока для приема сообщений от сервера
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    # Отправка сообщений на сервер
    while True:
        message = input()
        client_socket.sendall(message.encode('utf-8'))
