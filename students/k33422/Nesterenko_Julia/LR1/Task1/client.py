# Client side

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("127.0.0.1", 20000))  # подключаемся к сокету по указанному адресу
sock.send(b"Hello, server!")    # отправляем сообщение серверу
data = sock.recv(2048)    # получаем n байт данных от сервера
decoded_data = data.decode("utf-8")    # декодируем полученные данные
print("Recieved message:", decoded_data)
sock.close()