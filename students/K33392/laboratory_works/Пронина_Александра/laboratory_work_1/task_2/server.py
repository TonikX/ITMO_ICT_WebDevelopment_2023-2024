import socket
import math


def process_request(code_operation, params):
    if code_operation == 'a':
        a = float(params[0])
        b = float(params[1])
        c = math.sqrt(a ** 2 + b ** 2)
        return str(c)
    elif code_operation == 'b':
        a = float(params[0])
        b = float(params[1])
        c = float(params[2])
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return "x1 = " + str(x1) + ", x2 = " + str(x2)
        elif d == 0:
            x = -b / (2 * a)
            return "x = " + str(x)
        else:
            return "Уравнение не имеет корней, принадлежащих области действительных чисел"
    elif code_operation == 'c':
        a = float(params[0])
        b = float(params[1])
        h = float(params[2])
        s = (a + b) * h / 2
        return str(s)
    elif code_operation == 'd':
        a = float(params[0])
        h = float(params[1])
        s = a * h
        return str(s)
    else:
        return "Несуществующая операция"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)

while True:
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()

    print("Подключение от", client_address)

    request = client_socket.recv(1024).decode()
    operation, *parameters = request.split()

    result = process_request(operation, parameters)

    client_socket.send(result.encode())

    client_socket.close()
