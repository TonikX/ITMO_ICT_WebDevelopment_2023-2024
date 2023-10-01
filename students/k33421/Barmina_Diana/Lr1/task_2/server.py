import socket
import math


def solve_quad_eq(a, b, c): 
    D = b ** 2 - 4 * a * c
    sqrt_val = math.sqrt(abs(D))
    if D > 0:
        return (-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a)
    elif D == 0:
        return -b / (2 * a)
    else:
        return 'Нет корней'


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(("127.0.0.1", 14900))
        conn.listen(10)
        while True:
            client, address = conn.accept()
            client.sendall('Hello from server! Введите коэффициенты для квадратного уравнения через запятую'.encode('utf-8'))
            client_resp = client.recv(16384).decode('utf-8')
            #print(f'{client_resp}')
            try:
                a, b, c = map(float, client_resp.split(','))
                solve = str(solve_quad_eq(a, b, c)).encode('utf-8')
                client.sendall(solve)
            except:
                client.sendall("Неверно введены данные".encode('utf-8'))