import socket
from threading import Thread
from datetime import datetime
import random

serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024
name = random.choice(('Alex', 'Petya', 'Vasya', 'Timur', 'Ivan', 'Katya '))
# Создаем TCP сокет
TCPSocket = socket.socket()
# Подключаемся к серверу
TCPSocket.connect(serverAdress)
print("=== connected to the server ===\n")

def takeMessages(socket: socket.socket):
    while True:
        # Получем данные от сервера
        message = socket.recv(buffer).decode()
        print(f"\n{message}")

try:
    #запускаем мультипоток для получения сообщений с сервера
    thread = Thread(target = takeMessages, args = (TCPSocket, ))
    thread.daemon = True
    thread.start()

    while True:
        sendedMessage = input()
        
        if sendedMessage == "quit()":
            break

        timeOfMessage = datetime.now().strftime('%H:%M')
        sendedMessage = f"[{timeOfMessage}] {name}: {sendedMessage}"
        #отправляем сообщение серверу формата [дата] имя: ctx
        TCPSocket.send(sendedMessage.encode())
 
finally:
    print("\n=== Closing socket ===")
    TCPSocket.close()