import json
import socket


def main():
    while True:
        try:
            mes = input("Поиск площади параллелограмма (для завершения программы введите 'exit')\nВведите a,"
                        "h через пробел:\n")
            if mes.lower() == 'exit':
                break  # Выход из цикла при вводе 'exit'

            a, h = list(map(float, mes.split(" ")))  # ввод параметров
        except:
            print("Неверный ввод")
            continue

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # создание сокета
            sock.connect(('localhost', 1356))
            sock.send(bytes(json.dumps({"a": a, "h": h}), "utf-8"))  # отправка параметров
            data = sock.recv(1000).decode('utf-8')  # принятие и расшифровка ответа
            if not data:
                break
            print("Ответ: ", data)


if __name__ == "__main__":
    main()
