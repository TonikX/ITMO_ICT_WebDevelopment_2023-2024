# HTTP - Server side

import socket


# создаем сокет с семейством адресов IPv4 и использующим протокол TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 20000))    # связываем сокет с хостом и портом
sock.listen()
while True:
    connection, address = sock.accept()
    print("Connected to the client at", address)
    data = connection.recv(2048)    # получаем n байт данных от клиента
    decoded_data = data.decode("utf-8")    # декодируем полученные данные
    print("Recieved message from client:", decoded_data)
    with open("index.html") as index:
        starting_line = "HTTP/1.1 200 OK \n"
        headers = "Content-Type: text/html \n\n"
        message_body = index.read()
        response = (starting_line + headers + message_body).encode("utf-8")
    connection.send(response)    # посылаем ответ клиенту
    connection.close()