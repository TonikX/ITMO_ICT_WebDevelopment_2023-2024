import socket
import threading

# Создаем TCP-клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

# Вводим имя пользователя
client_name = input("Введите ваше имя: ")

client_socket.connect(server_address)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f"Ошибка: {e}")
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    if message.lower() == "exit":
        break

    client_socket.send(f"{client_name}: {message}".encode())

client_socket.close()
