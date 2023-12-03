import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

try:
    base1 = float(input("Введите длину первого основания: "))
    base2 = float(input("Введите длину второго основания: "))
    height = float(input("Введите высоту трапеции: "))

    data_to_send = f"{base1},{base2},{height}"
    sock.send(data_to_send.encode())

    data = sock.recv(1024)
    decoded_data = data.decode("utf-8")
    print("Площадь трапеции, вычисленная сервером:", decoded_data)
except ValueError:
    print("Ошибка: Введите корректные числа.")

sock.close()
