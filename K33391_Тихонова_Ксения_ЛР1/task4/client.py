import socket
from threading import Thread


def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except:
            break


def respond():
    while True:
        client.send((input()).encode('utf-8'))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_adress = ('localhost', 7777)

client.connect(client_adress)

username = input('Введите имя: ')

rec_thread = Thread(target=receive)
rec_thread.start()

client.send(username.encode('utf-8'))
respond()