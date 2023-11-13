import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
s.connect((host, port))
name = input('Enter your name: ')
s.sendall(name.encode())

def receiver(): #Function for receiving the data
    while True:
        res = s.recv(1024)
        print(res.decode())

def sender(): #Function for sending the data
    while True:
        msg = input()
        s.send(msg.encode())

r_thr = threading.Thread(target=receiver).start()
s_thr = threading.Thread(target=sender).start()
