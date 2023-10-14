import socket

# UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Hello, client'.encode()

server_address = ('localhost', 10000)  #
udp_socket.bind(server_address)

while True:
    data, address = udp_socket.recvfrom(1024)
    print(f'Получено сообщение от {address}: {data.decode()}')

    udp_socket.sendto(message, address)