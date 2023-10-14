import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Hello, server'.encode()

server_address = ('localhost', 10000)

try:
    print('Отправка {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    data, server = sock.recvfrom(4096)
    print('Получено {!r}'.format(data))

except Exception as e:
    print(f'Произошла ошибка: {e}')

finally:
    sock.close()
