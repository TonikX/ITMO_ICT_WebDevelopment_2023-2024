import socket

serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024

# Подключаемся к серверу, получаем сокет
TCPSocket = socket.create_connection(serverAdress)
 
try:
    data = input("Введите высоту и основание параллелограмма:")
    data = str.encode(data)
    # Отправляем данные, введенные с клавиатуры
    TCPSocket.sendall(data)
    # Получем ответ от сервера
    data = TCPSocket.recv(buffer)
    data = data.decode("utf-8")
    print("Площадь параллелограмма: {}".format(data))
 
finally:
    print("Closing socket")
    # Закрываем подключение
    TCPSocket.close()