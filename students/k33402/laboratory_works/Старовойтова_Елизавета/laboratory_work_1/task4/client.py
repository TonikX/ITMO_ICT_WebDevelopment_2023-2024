import threading
import socket

host = "127.0.0.1"
port = 59000
buffSize = 1024

alias = input("Choose an alias >>> ")
tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientSock.connect((host, port))


def client_receive():
    while True:
        try:
            message = tcpClientSock.recv(buffSize).decode("utf-8")
            if message == "alias?":
                tcpClientSock.send(alias.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error!")
            tcpClientSock.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        tcpClientSock.send(message.encode("utf-8"))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
