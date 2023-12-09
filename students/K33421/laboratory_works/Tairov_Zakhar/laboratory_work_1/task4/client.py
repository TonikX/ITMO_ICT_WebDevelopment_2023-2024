import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

def recv_broadcast(client_sock):
    while True:
        try:
            msg = client_sock.recv(1024).decode()
            print(msg)
        except:
            break

def send_msg(client_sock, name):
    while True:
        print(f"[{name}]> ", end="")
        msg = input()
        client_sock.send(msg.encode())
try:
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET.connect((HOST, PORT))
    name = input("Register your chat handle: ")
    SOCKET.send(name.encode())
    threading.Thread(target=recv_broadcast, args=(SOCKET,)).start()
    threading.Thread(target=send_msg, args=(SOCKET, name)).start()
except KeyboardInterrupt:
    exit()