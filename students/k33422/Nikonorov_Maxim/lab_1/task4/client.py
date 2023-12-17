import socket
import threading

nickname = input('Введи свой никнейм: ')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 49001))  

def client_recieve():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == "nickname?":
                sock.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error")
            sock.close()
            break

def client_send():
    while True:
        message = f'{nickname}: {input()}'
        sock.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target = client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()
