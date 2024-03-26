import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
a, b = map(int, input('Введите два числа через пробел: ').split())
sock.send(bytes([a, b]))

data = sock.recv(1024)
if data:
    print(data.decode('utf8'))
else:
    print('Соединение прервано')

sock.close()
