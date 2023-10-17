import socket


def main():
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))

        data = f"{a} {b} {c}"
        client_socket.send(data.encode())

        result = client_socket.recv(1024).decode()
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
