import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('Сервер запущен и ожидает сообщения от клиента...')

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode('utf-8')

    print('Получено сообщение от клиента:', message)

    response = 'Hello, client'
    server_socket.sendto(response.encode('utf-8'), client_address)