import socket

server = socket.socket()
server.bind(('', 9090))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(1024)
if not data:
    print('Соединение прервано')
else:
    conn.send(bytearray(f'Гипотенуза равна {(data[0] ** 2 + data[1] ** 2) ** 0.5}', 'utf8'))

conn.close()