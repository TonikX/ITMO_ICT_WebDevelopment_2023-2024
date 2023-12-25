import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 3000)
    client_socket.connect(server_address)

    base1 = float(input("Введите длину первого основания: "))
    base2 = float(input("Введите длину второго основания: "))
    height = float(input("Введите высоту: "))

    data = f"{base1},{base2},{height}"
    client_socket.send(data.encode("utf-8"))

    result = client_socket.recv(1024).decode("utf-8")
    print(f"Площадь трапеции: {result}")

    client_socket.close()


if __name__ == "__main__":
    main()
