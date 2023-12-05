import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5555))

client_name = input("Введите ваше имя: ")
client_socket.send(client_name.encode('utf-8'))


def send_message():
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                client_socket.close()
                print("Выход из чата")
                break
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")
        client_socket.close()


def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            client_socket.close()
            print("Сервер отключился")
            break


send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
