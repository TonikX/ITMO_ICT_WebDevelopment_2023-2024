import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

client_socket.connect(server_address)
print('Подключено к серверу:', server_address)

base = float(input('Введите значение основания: '))
height = float(input('Введите значение высоты: '))

if base < 0 or height < 0:
    print('Высота и длина не могут быть отрицательными.')
    client_socket.close()
    exit()

client_socket.send(str(base).encode('utf-8'))
client_socket.send(str(height).encode('utf-8'))

result = client_socket.recv(1024).decode('utf-8')

print('Результат операции:', result)

client_socket.close()