import socket
import threading

# Задание никнейма
nickname = input("Choose your nickname: ")

# Соединение с сервером
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


# Прослушивание сервера
def receive():
    while True:
        try:
            # Получение сообщения от сервера
            # Если было отправлено 'NICK',
            # отправим в ответ серверу никнейм,
            # а иначе выведем текст сообщения
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Закрытие соединения
            print("An error occured!")
            client.close()
            break


# Отправка сообщений на сервер
def write():
    while True:
        client.send(f'{nickname}: {input()}'.encode('ascii'))


# Запуск потоков для чтения и отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
