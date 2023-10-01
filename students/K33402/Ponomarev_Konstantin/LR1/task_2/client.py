import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    client_socket.connect(server_address)

    first_cathetus = float(input("Введите длину первого катета: "))
    second_cathetus = float(input("Введите длину второго катета: "))

    data = str([first_cathetus, second_cathetus]).encode("utf-8")
    client_socket.send(data)

    result = client_socket.recv(1024).decode("utf-8")
    print(f"гипотенуза в прямоугольном треугольнике: {result}")

    client_socket.close()


if __name__ == "__main__":
    main()
