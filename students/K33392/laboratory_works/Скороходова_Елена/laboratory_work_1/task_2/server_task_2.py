import json
import socket


def get_parallelogram_area(a, h):
    s = a * h
    return s


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создание сокета
    sock.bind(('localhost', 1356))  # связь сокета с хостом и портом
    print("Сервер запущен и ожидает входящих данных...")
    sock.listen(5)

    while True:
        try:
            client_socket, addr = sock.accept()  # новый сокет и адрес клиента
            data = client_socket.recv(1024)

            if data != "":
                udata = json.loads(data.decode('utf-8'))  # декодирование строки
                a = udata.get('a')
                h = udata.get('h')
                print("Получены данные от клиента")
                reply_msg = get_parallelogram_area(a, h)
                reply_msg_bytes = str(reply_msg).encode('utf-8')
                client_socket.send(reply_msg_bytes)
                print("Отправлен ответ")

        except KeyboardInterrupt:
            sock.close()
            print("Соединение закрыто")


if __name__ == "__main__":
    main()
