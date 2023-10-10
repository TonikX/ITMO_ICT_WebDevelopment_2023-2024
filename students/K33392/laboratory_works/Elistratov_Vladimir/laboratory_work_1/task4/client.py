import socket
import random
import threading
from time import sleep

#names = ['HappyWolf', 'stasok56', 'ElricDeRay', 'Glavk2 \"Gasmask \"', 'AE DOMINUS NOX', 'Zerg', 'XarD']
#ictionary = ['Hello', 'Abra Cadabra', 'Crible Krable Booms', 'Perestroika', 'Maybe you\'ll be lucky', 'Buy', 'Hobbit']

name = input("Enter your name: ")

serverIP = "192.168.56.1"
PORT = 14900
buffSize = 16384

session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
session.connect((serverIP, PORT))

def messWait():
    while True:
        data = session.recv(buffSize)
        print(data.decode("utf-8"))

listenerClient = threading.Thread(target=messWait)
listenerClient.daemon = True
listenerClient.start()

while True:
    ms = input()
    ms = name + ': ' + ms
    session.send(ms.encode('utf-8'))
    if(ms == (name + ": " + "exit_T")):
        break


#connection.close()