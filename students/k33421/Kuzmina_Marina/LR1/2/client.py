import socket

# Создаем TCP-клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

try:
    # Вводим данные с клавиатуры
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину второго катета: "))

    # Отправляем данные серверу
    message = f"{a},{b}"
    client_socket.connect(server_address)
    client_socket.send(message.encode())

    # Получаем и выводим ответ от сервера
    data = client_socket.recv(1024).decode()
    print(f"Ответ от сервера: {data}")
except ValueError:
    print("Ошибка: Введите числовые значения для длин катетов.")
finally:
    client_socket.close()
