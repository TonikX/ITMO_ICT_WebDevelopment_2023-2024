import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 49001)) 

print('Введите коэфициенты a, b, c через проблел:')

try:
    a, b, c = map(str, input().split())
    coef = a + ' ' + b + ' ' + c
    sock.send(coef.encode())
    data = sock.recv(1024).decode("utf-8")
    print(data)
except:
    print('Какая-то ошибка')
    sock.close()

