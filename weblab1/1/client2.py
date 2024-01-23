import socket

server_address = ('localhost', 55555)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    socket.sendto(msg.encode(), server_address)
    if msg == 'exit':
        break
    else:
        data, address = socket.recvfrom(128)
        data = data.decode()
        print(data)

socket.close()
