import socket


def calculate_trapezoid_area(base1, base2, height):
    return ((base1 + base2) * height) / 2


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5434)
server_socket.bind(server_address)
server_socket.listen(5)

print("Сервер запущен")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключено клиентское соединение с {client_address}")

    data = client_socket.recv(1024).decode()
    print(f"Получено сообщение от клиента: {data}")

    params = data.split(',')
    if len(params) != 3:
        response = "Неправильный формат данных. Используйте формат 'base1,base2,height'"
    else:
        try:
            base1, base2, height = map(float, params)
            area = calculate_trapezoid_area(base1, base2, height)
            response = f"Площадь трапеции: {area}"
        except ValueError:
            response = "Ошибка"

    client_socket.send(response.encode())
    client_socket.close()
