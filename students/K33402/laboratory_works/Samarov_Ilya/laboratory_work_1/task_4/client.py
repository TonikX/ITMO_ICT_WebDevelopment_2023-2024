import socket
import threading
import sys

def send_message():
    while True:
        message = input()
        c_socket.send(message.encode())

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = ('localhost', 12412)
c_socket.connect(s_address)
send_thread = threading.Thread(target=send_message)
send_thread.start()

while True:
    try:
        message = c_socket.recv(1024).decode()
        print(message)
    except Exception as e:
        print(f'Ошибка при получении сообщения: {str(e)}')
        break

c_socket.close()