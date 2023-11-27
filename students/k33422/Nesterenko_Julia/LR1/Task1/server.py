# Server side

import socket


# создаем сокет с семейством адресов IPv4 и использующим протокол UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 20000))    # связываем сокет с хостом и портом
data, addr = sock.recvfrom(2048)    # получаем n байт данных от клиента
decoded_data = data.decode("utf-8")    # декодируем полученные данные
print("Recieved message:", decoded_data)
sock.sendto(b"Hello, client!", addr)    # посылаем ответ клиенту
sock.close()