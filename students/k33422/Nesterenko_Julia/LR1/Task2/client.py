# Pythagoras Theorem - Client side

import socket


print("Pythagoras Theorem Calculation")
a, b = input("Enter leg a length: "), input("Enter leg b length: ")
if (a + b).isdigit():
    msg = (a + " " + b).encode("utf-8")
else:
    raise ValueError("Triangle legs lengths must be positive integers")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 20000))  # подключаемся к сокету по указанному адресу
sock.send(msg)    # отправляем сообщение серверу
data = sock.recv(2048)    # получаем n байт данных от сервера
decoded_data = data.decode("utf-8")    # декодируем полученные данные
print("Hypotenuse c length:", decoded_data)
sock.close()