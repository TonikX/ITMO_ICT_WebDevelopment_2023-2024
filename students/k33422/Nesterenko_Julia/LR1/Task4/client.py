# Multiprocessing - Client side

import socket
from threading import Thread


#   получение сообщений
def receive():
    while True:
        try:
            data = sock.recv(2048)
            message = data.decode("utf-8")
            if message == 'nickname':
                sock.send(name.encode("utf-8"))
            else:
                print(message)
        except:
            print(f"Oops! An error occurred. Try again later")
            sock.close()
            break


#   отправка сообщений
def respond():
    while True:
        try:
            message = input()
            sock.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Oops! An error occurred. Try again later\nError details: {e}")
            sock.close()
            break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 20000))

name = input("Welcome to the chat.\nEnter your nickname: ")

receive_th = Thread(target=receive)
receive_th.start()
respond_th = Thread(target=respond)
respond_th.start()
