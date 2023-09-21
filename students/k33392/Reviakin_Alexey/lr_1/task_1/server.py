import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind((socket.gethostname(), 12345))  # открытие сокета

data, addres = conn.recvfrom(1024)  # получение данных клиента
udata = data.decode("utf-8")  # декодирование данных
print(f"{udata}")  # печать данных на стороне сервера
conn.sendto(b"Hello, client", addres)  # отправка данных клиенту
conn.close()  # закртыие сокета
