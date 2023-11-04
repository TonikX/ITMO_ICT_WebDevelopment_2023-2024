import socket
from threading import Thread
from datetime import datetime
from Lab1.serverConfigurator import ServerConfigurator


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


server_config = ServerConfigurator.default_configuration()
separator_token = "<SEP>"
s = socket.socket()
s.connect(server_config)
print("[+] Connected.")

name = input("Enter your name: ")

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    s.send(to_send.encode())

s.close()