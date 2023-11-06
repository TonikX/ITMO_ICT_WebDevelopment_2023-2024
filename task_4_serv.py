import socket
import threading

# Список для хранения подключенных клиентов
clients = []

# Создаем сокет TCP
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
s_address = ('localhost', 12345)
s_socket.bind(s_address)

# Ожидаем соединений клиентов
s_socket.listen(5)
print('Сервер ожидает подключения клиентов...')

# Функция для обработки клиентских сообщений
def handle_client(c_socket):
    while True:
        try:
            message = c_socket.recv(1024).decode()
            if not message:
                # Если сообщение пустое, клиент отключился, удаляем его из списка
                clients.remove(c_socket)
                c_socket.close()
                break
            print(f'Получено сообщение: {message}')
            # Отправляем сообщение всем клиентам, кроме отправителя
            for client in clients:
                if client != c_socket:
                    client.send(message.encode())
        except Exception as e:
            print(f'Ошибка при обработке сообщения: {str(e)}')

while True:
    # Принимаем соединение от клиента
    c_socket, c_address = s_socket.accept()
    print(f'Подключен клиент: {c_address}')

    # Добавляем клиента в список
    clients.append(c_socket)

    # Запускаем поток для обработки сообщений клиента
    client_thread = threading.Thread(target=handle_client, args=(c_socket,))
    client_thread.start()
