import socket
import threading

# Функция для отправки сообщений
def send_message():
    while True:
        message = input()
        c_socket.send(message.encode())

# Создаем сокет TCP
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Адрес и порт сервера
s_address = ('localhost', 12345)

# Подключаемся к серверу
c_socket.connect(s_address)

# Запускаем поток для отправки сообщений
send_thread = threading.Thread(target=send_message)
send_thread.start()

while True:
    try:
        # Получаем сообщения от сервера
        message = c_socket.recv(1024).decode()
        print(message)
    except Exception as e:
        print(f'Ошибка при получении сообщения: {str(e)}')
        break

# Закрываем сокет клиента
c_socket.close()
