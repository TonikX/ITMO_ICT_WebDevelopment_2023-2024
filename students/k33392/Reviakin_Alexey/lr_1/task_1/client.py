import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect((socket.gethostname(), 12345))  # подключение к серверу
conn.send(b"Hello, Server!")  # опарвка данных на сервер
data = conn.recv(1024)  # получение данных от сервера
udata = data.decode("utf-8")  # раскодировка данных
print(f"{udata}")  # печать данных на стороне клиента
