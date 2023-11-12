import socket


def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)

print("Сервер ожидает подключения...")

while True:
    connection, client_address = sock.accept()
    print(f"Подключено клиентом: {client_address}")

    try:
        data = connection.recv(1024)
        decoded_data = data.decode("utf-8")


        base1, base2, height = map(float, decoded_data.split(','))


        result = calculate_trapezoid_area(base1, base2, height)


        connection.send(str(result).encode())
        print(f"Отправлен результат {result} клиенту: {client_address}")
    except ValueError:
        print("Ошибка: Некорректные данные от клиента.")
    break


    connection.close()
