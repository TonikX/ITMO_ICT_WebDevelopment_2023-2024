import socket
from math import sqrt

def calculate_discriminant(a, b, c):
    return b ** 2 - 4 * a * c

def get_answer(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:
        return 'Error'
    elif discriminant == 0:
        x = -(b) / (2 * a)
        return str(x)
    else:
        x1 = (-(b) + sqrt(discriminant)) / (2 * a)
        x2 = (-(b) - sqrt(discriminant)) / (2 * a)
        return f"{x1}, {x2}"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 14900))

data, client_address = server.recvfrom(16384)
coefficients = list(map(int, data.decode("UTF-8").split()))

answer = get_answer(*coefficients)
server.sendto(bytes(answer, 'UTF-8'), client_address)

server.close()