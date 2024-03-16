import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    print('Ожидание сообщения от клиента...')
    data, client_address = server_socket.recvfrom(1024)
    print(f'Получено от клиента: {data.decode()}')
    response_message = 'Привет, клиент!'
    server_socket.sendto(response_message.encode(), client_address)
