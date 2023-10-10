import socket
from threading import Thread
from datetime import datetime
import random

serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024
name = random.choice(('Alex', 'Petya', 'Vasya', 'Timur', 'Ivan', 'Katya '))

TCPSocket = socket.socket()
TCPSocket.connect(serverAdress)
print("=== connected to the server ===\n")

def takeMessages(socket: socket.socket):
    while True:
        message = socket.recv(buffer).decode()
        print(f"\n{message}")

try:
    thread = Thread(target = takeMessages, args = (TCPSocket, ))
    thread.daemon = True
    thread.start()

    while True:
        sendedMessage = input()
        
        if sendedMessage == "quit()":
            break

        timeOfMessage = datetime.now().strftime('%H:%M')
        sendedMessage = f"[{timeOfMessage}] {name}: {sendedMessage}"
        TCPSocket.send(sendedMessage.encode())
 
finally:
    print("\n=== Closing socket ===")
    TCPSocket.close()


