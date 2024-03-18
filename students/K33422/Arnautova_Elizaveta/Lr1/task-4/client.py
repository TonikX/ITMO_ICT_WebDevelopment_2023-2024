import socket
import threading

HOST = '127.0.0.1'
SERVER_PORT = 14901
BUFF_SIZE = 16384

name = input("What is your name? ")  # запрос имени пользователя
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание TCP сокета клиента
client.connect((HOST, SERVER_PORT))  # подключение клиента к указанному хосту и порту


def input_information():  # обрабатывает входящую информацию от сервера
    while True:  # ожидает получение сообщения от сервера
        try:
            message = client.recv(BUFF_SIZE).decode('utf-8')
            if message == 'name':  # Если получено сообщение 'name', клиент отправляет свое имя на сервер
                client.send(name.encode('utf-8'))
            else:  # В противном случае, сообщение выводится в консоль
                print(message)

        except:
            client.close()
            break


def output_information():  # обрабатывает исходящую информацию от клиента
    while True:
        message = input('')  # ожидает ввод сообщения от пользователя
        if message == 'leave':                              # Если введено сообщение 'leave',
            client.send(f'*{name} left*'.encode('utf-8'))   # клиент отправляет сообщение о своем уходе на сервер
            client.close()                                  # и закрывает соединение
            break

        message = '{}: {}'.format(name, message)    # иначе сообщение форматируется как "{имя}: {сообщение}"
        client.send(message.encode('utf-8'))        # и отправляется на сервер


receive_thread = threading.Thread(target=input_information)  # создание потока для функции input_information
receive_thread.start()

write_thread = threading.Thread(target=output_information)  # создание потока для функции output_information
write_thread.start()
