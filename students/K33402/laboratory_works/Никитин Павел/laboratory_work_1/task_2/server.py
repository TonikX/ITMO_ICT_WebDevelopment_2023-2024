import socket


def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 3000)
    server_socket.bind(server_address)

    # Ожидаем соединения клиента
    server_socket.listen(1)
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент: {client_address}")

    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            params = data.split(",")
            if len(params) == 3:
                base1, base2, height = map(float, params)
                result = calculate_trapezoid_area(base1, base2, height)
                client_socket.send(str(result).encode("utf-8"))
            else:
                client_socket.send("Неверные параметры. Ожидается основание1, основание2, высота".encode("utf-8"))
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            break

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
