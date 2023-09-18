# Pythagoras Theorem - Server side

import socket


def calculate_hypotenuse(pair):
    a, b = map(int, pair.split(' '))
    c = (a**2 + b**2)**(1/2)
    return str(c)


# создаем сокет с семейством адресов IPv4 и использующим протокол TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 20000))    # связываем сокет с хостом и портом
sock.listen()
connection, address = sock.accept()
data = connection.recv(2048)    # получаем n байт данных от клиента
decoded_data = data.decode("utf-8")    # декодируем полученные данные
print("Recieved a and b lengths:", decoded_data)
reply = calculate_hypotenuse(decoded_data).encode("utf-8")
connection.send(reply)    # посылаем ответ клиенту
connection.close()