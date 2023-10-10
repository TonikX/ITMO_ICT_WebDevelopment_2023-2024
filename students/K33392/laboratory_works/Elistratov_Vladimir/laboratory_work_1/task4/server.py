import socket
import threading
from time import sleep

IP = "127.0.0.1"

PORT = 14900
buffSize = 16384

session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
session.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = socket.gethostbyname(socket.gethostname())

session.bind((IP, PORT))
session.listen(10)

userList = []

def listener(cSession):
    while True:
        ms = cSession.recv(buffSize).decode('utf-8')
        for i in userList:
            i.send(ms.encode('utf-8'))
        
        if(ms.find("exit_T") != -1):
            #print("EXIT")
            #print(ms, ' ', ms.find("exit_t"), '\n')
            userList.remove(cSession)
            break

while True:
    client_conn, address = session.accept()
    
    userList.append(client_conn)

    clientsServer = threading.Thread(target=listener, args=(client_conn,))
    clientsServer.daemon = True
    clientsServer.start()


