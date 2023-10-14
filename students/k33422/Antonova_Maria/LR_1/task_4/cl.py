import socket #модуль сокетов для работы с сетью
import threading #модуль  для создания потоков

def receive_messages(client_socket): #прием сообщений от сервера
    while True:
        data = client_socket.recv(1024).decode() #принимаем сообщение от сервера и декодируем встр
        if not data:
            break
        print(data) #выводим сообщение сервера в консоль

def client_program():
    host = socket.gethostname()
    port = 15000
    client_socket = socket.socket() #создаем сокет клиента
    client_socket.connect((host, port)) #подключаемся к серверу по указанному хосту и порту
    print("Connected to the server.")

    # поток для приема сообщений от сервера
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,)) # создаем новый поток и передаем в него сокет клиента для приема сообщений
    receive_thread.start()

    while True:
        message = input(" -> ")
        client_socket.send(message.encode()) #отправляем введенное сообщение серверу
        if message.lower().strip() == 'bye':
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()
