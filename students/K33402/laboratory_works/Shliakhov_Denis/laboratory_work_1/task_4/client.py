import socket
import threading

nickname = input("Введите ваш ник: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 9090))
print("Подключен к чату")


def get_message():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "nickname":
                client.send(nickname.encode())
            else:
                print(message)
        except Exception as e:
            print(e)
            client.close()
            break


def send_message():
    while True:
        message = input("").encode()
        client.send(message)


get_thread = threading.Thread(target=get_message)
get_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
