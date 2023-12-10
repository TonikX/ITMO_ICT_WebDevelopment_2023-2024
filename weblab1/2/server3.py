import socket
import math


def get_message():
    data = connection.recv(128).decode()
    log_file.write(f'Message from {address[0]}:{address[1]}: {data}\n')
    return data


def send_message(msg):
    connection.send(msg.encode())
    log_file.write(f'Message to {address[0]}:{address[1]}: {msg}\n')


def find_roots(coefficients):
    a, b, c = map(float, coefficients.split())
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return 'This equation has no real roots'
    x1 = (b * (-1) + math.sqrt(discriminant)) / (2 * a)
    x2 = (b * (-1) - math.sqrt(discriminant)) / (2 * a)
    if x1 == x2:
        return f'This equation has one root: {x1}'
    else:
        return f'Roots of this equation are: {x1} and {x2}'


log_file = open("server3.log", "w")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 55555))

socket.listen(1)
connection, address = socket.accept()
send_message('Please type \'Find equation roots\' to find roots of your quadratic equation'
             '\nType \'exit\' to terminate connection')

while True:
    message = get_message()

    if message == 'Find equation roots':
        send_message('Enter equation coefficients\nExample: 1 4 3')

        coefficients = get_message()
        answer = find_roots(coefficients)

        send_message(answer)
    elif message == 'exit':
        break
    else:
        send_message('No understanding')

socket.close()

