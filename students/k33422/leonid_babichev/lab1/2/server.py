import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print('Сервер запущен и ожидает подключения клиента...')

while True:
    client_socket, client_address = server_socket.accept()
    print('Подключился клиент:', client_address)

    base = float(client_socket.recv(1024).decode('utf-8'))
    height = float(client_socket.recv(1024).decode('utf-8'))

    area = base * height

    client_socket.send(str(area).encode('utf-8'))

    client_socket.close()