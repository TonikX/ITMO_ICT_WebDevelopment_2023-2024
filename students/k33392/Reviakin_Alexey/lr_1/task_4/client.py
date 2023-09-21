import socket
import threading

conn = socket.socket()

name = input("Введите имя\n")

conn.connect((socket.gethostname(), 2347))
conn.setblocking(0)


def listen_msg():
    while True:
        message = conn.recv(1024).decode()
        print("\n" + message)


t = threading.Thread(target=listen_msg)
t.start()

while True:
    msg = input()
    if msg == "q":
        break
    conn.send(f"{name}: {msg}".encode("utf-8"))

conn.close()
