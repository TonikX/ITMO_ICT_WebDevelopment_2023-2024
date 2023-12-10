import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('localhost', 55555))

while True:
    data, address = socket.recvfrom(128)
    data = data.decode()
    print(f'Message from {address[0]}:{address[1]}: {data}')
    if data == 'Hello, server':
        socket.sendto('Hello, client'.encode(), address)
    elif data == 'exit':
        break
    else:
        socket.sendto('No understanding'.encode(), address)

socket.close()
