# Импортируем необходимые модули для сокетов и многопоточности
import socket
import threading

# Запрашиваем у пользователя выбор никнейма
nickname = input('Choose a nickname: ')

# Создаем сокет клиента, используя IPv4 и TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаемся к серверу по адресу localhost и порту 9991
client.connect(('localhost', 9991))


# Функция для приема сообщений от сервера
def receive():
    while True:  # Бесконечный цикл для постоянного приема сообщений
        try:
            # Принимаем сообщение от сервера размером до 1024 байт и декодируем его
            message = client.recv(1024).decode('utf-8')
            if message == 'Nick':  # Если сообщение запрос на никнейм,
                client.send(nickname.encode('utf-8'))  # отправляем наш никнейм обратно на сервер
            else:
                print(message)  # В противном случае, выводим полученное сообщение
        except:
            print('An error occurred.')  # В случае ошибки выводим сообщение об ошибке
            client.close()  # Закрываем соединение с сервером
            break  # Выходим из цикла


# Функция для отправки сообщений на сервер
def write_message():
    while True:  # Бесконечный цикл для возможности отправки сообщений
        # Считываем сообщение от пользователя и формируем строку с никнеймом
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))  # Отправляем сообщение на сервер в кодировке utf-8


# Создаем поток для приема сообщений, чтобы не блокировать основной поток выполнения
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Создаем поток для отправки сообщений, чтобы можно было одновременно отправлять и получать сообщения
write_thread = threading.Thread(target=write_message)
write_thread.start()
