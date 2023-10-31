from socket import *
from math import sqrt


def find_hip(data: [int]):
    a = data[0]
    b = data[1]
    c = sqrt(a**2 + b**2)
    return c


def find_cat(data: [int]):
    c = data[0]
    a = data[1]
    b = sqrt(c**2 - a**2)
    return b


hello_message = "Вас приветствует сервер для решения теоремы пифагора.\n " \
                "Пожалуйста, при помощи цифры выберете, что вы хотите найти:\n" \
                "1) Гипотенузу \n" \
                "2) Катет".encode()


# Настраиваем хост
host = gethostname()
port = 10000
host_data = (host, port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(host_data)
server_socket.listen()

conn, addr = server_socket.accept()
conn.sendall(hello_message)

request = conn.recv(1024).decode()

# Обработать запрос и все посчитать
operation_type = int(request[0])
request = request[1:]
data = list(map(int, request.split(",")))

result = ""
if operation_type == 1:
    answer = find_hip(data)
    result = "Значение гипотенузы равно " + str(answer)
else:
    answer = find_cat(data)
    result = "Значение катета равно " + str(answer)

conn.sendall(result.encode())
conn.close()

