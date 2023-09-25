import socket
import threading
import time
from datetime import datetime

usersDict = {}
oldMessages = []
newMessages = []


class Message():
    def __init__(self,userName, userSocket, text):
        self.userName = userName
        self.userSocket = userSocket
        self.text = text
        self.status  = 0
    def make_text(self):
        return self.userName+": "+self.text







class ClientThread(threading.Thread):
    def __init__(self, clientAdress, clientSocket):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientAdress = clientAdress
        self.connection = True
        self.userName = "Default User"
        usersDict[self.clientSocket] = self.clientAdress

    def break_connection(self):
        usersDict.pop(self.clientSocket)
        self.clientSocket.close()
        self.connection = False

    def listen(self):
        print(f"Start listening to {self.userName}")
        counter = 0
        while self.connection:
            msg = self.clientSocket.recv(16384)
            msg = msg.decode("UTF-8")
            if msg:
                counter = 0
                #last_time = datetime.now()
                print(self.userName+': ' + msg)
                msg = Message(self.userName,self.clientSocket,msg)
                newMessages.append(msg)

            else:
                counter+=1
            #elif datetime.now().second - last_time.second > 20 or datetime.now().second - last_time.second < -40:
            if counter>=10:
                print(f"The {self.userName} was blocked")
                #clientSocket.send(bytes("Enjoy the silence, bye", "UTF-8")) # вопрос, почему не вылетает ошибка, если клиент сам разорвал сообщение?
                self.break_connection()
                break
        print(f"End listening to {self.userName}")
    # def send(self):
    #     print(f"Start sending to {self.userName}")
    #     while self.connection:
    #         msg = input()
    #         if self.connection:
    #             self.clientSocket.send(bytes(msg, "UTF-8"))
    #     print(f"End sending to {self.userName}")

    def run(self):
        try:
            self.clientSocket.send(bytes("Please, enter your name...", "UTF-8"))
            if self.connection:
                msg = self.clientSocket.recv(16384)
            else:
                self.break_connection()
                return
            self.userName = msg.decode("UTF-8")
            print(msg.decode("UTF-8"))
            # сделать так, чтобы остальные потоки остановились, пока выполняется эта часть
            for message in oldMessages:
                self.clientSocket.send(bytes(message.make_text(), "UTF-8"))

            self.listen()
            #ear = threading.Thread(target=self.listen)
            #ear.start()
            #mouth = threading.Thread(target=self.send)
            #mouth.start()

        except:
            print(f"Connection with {self.userName} was broken ")
            self.break_connection()


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('', 2002))
server.listen(10)


def sending():
    time.sleep(2)
    while True:
        try:
            for user in usersDict.keys():
                for new_message in newMessages:
                    if new_message.userSocket != user:
                        user.send((bytes(new_message.make_text(), "UTF-8")))
            newMessages.clear()
        except:
            print("Let's try again")

while True:
    clientSocket, clientAdress = server.accept()
    print("WE HAVE A NEW USER")
    newThread = ClientThread(clientAdress, clientSocket)
    threadForSending = threading.Thread(target=sending)
    newThread.start()
    threadForSending.start()