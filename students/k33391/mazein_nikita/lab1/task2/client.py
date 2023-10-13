import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1337))

while True:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))

    data = '{} {} {}'.format(a, b, c)
    s.send(data.encode('utf-8'))
    print('Sent data to server:', data)

    response = s.recv(1024)
    print('Received data from server:', response.decode('utf-8'))

    if input('Do you want to continue? [y/n] ') == 'n':
        break

s.close()