import math
import socket


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return "Два корня: x1 = {}, x2 = {}".format(x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return "Один корень: x = {}".format(x)
    else:
        return "Нет действительных корней"


def start_server(host, port):
    server_address = (host, port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        print("Ожидание подключения клиента...")
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            a, b, c = map(float, data.split())
            result = solve_quadratic(a, b, c)
            client_socket.send(result.encode())
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
        finally:
            client_socket.close()


def main():
    server_host = '127.0.0.1'
    server_port = 12345
    start_server(server_host, server_port)


if __name__ == "__main__":
    main()
