import socket

if __name__ == "__main__":
    # Задаем IP-адрес и порт сервера, к которому будем подключаться.
    server_ip = '127.0.0.1'
    server_port = 6998

    # Создаем TCP сокет (SOCK_STREAM) и устанавливаем соединение с сервером.
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_ip, server_port))

    # Запрашиваем у пользователя выбор операции (cath/hyp или c/h).
    operation = input("Выберите опцию (cath/hyp или c/h): ")

    # Проверяем, что пользователь ввел корректную операцию.
    while operation not in ["cath", "c", "hyp", "h"]:
        operation = input("Неверная операция. Попробуйте снова: ")

    # Преобразуем сокращенные операции в полные.
    if operation in ("c", "h"):
        operation = "cath" if operation == "c" else "hyp"

    # Вводим значения сторон треугольника с обработкой ошибок.
    while True:
        if operation == "cath":
            a = input("Введите катет: ")
            b = input("Введите гипотенузу: ")
        else:
            a = input("Введите катет: ")
            b = input("Введите катет: ")
        try:
            a = float(a)
            b = float(b)
            break
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")

    # Отправляем операцию и значения сторон на сервер.
    conn.send(bytes(f"{operation}, {a}, {b}", encoding="utf-8"))

    # Получаем и выводим результат от сервера.
    result = conn.recv(1024).decode("utf-8")
    print(f"Результат: {result}")

