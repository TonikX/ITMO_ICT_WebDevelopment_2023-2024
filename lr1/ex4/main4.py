import threading
import socket

def handle_server(server_socket):
    while True:
        try:
            message = server_socket.recv(1024).decode('utf-8')
            if message:
                print('\n' + message)
        except:
            print('Потеряно соединение с сервером')
            server_socket.close()
            break

def start_client():
    client_name = input('Введите ваше имя: ')

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.send(client_name.encode('utf-8'))

    client_thread = threading.Thread(target=handle_server, args=(client_socket,))
    client_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

client_thread = threading.Thread(target=start_client)
client_thread.start()
