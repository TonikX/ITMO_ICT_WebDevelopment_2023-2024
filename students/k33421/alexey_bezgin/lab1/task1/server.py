import socket

if __name__ == "__main__":
    # Задаем IP-адрес и порт сервера, на котором будем слушать входящие сообщения.
    server_ip = '127.0.0.1'
    server_port = 7000

    # Создаем UDP сокет (SOCK_DGRAM) и связываем его с указанным IP-адресом и портом.
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind((server_ip, server_port))

    # Бесконечный цикл для прослушивания входящих сообщений.
    while True:
        # Получаем данные и адрес отправителя.
        data, addr = conn.recvfrom(1024)

        # Выводим полученные данные (раскодированные из байтовой строки) на экран.
        print(data.decode("utf-8"))

        # Отправляем ответное сообщение "Hello, client" обратно клиенту по адресу отправителя.
        conn.sendto(b"Hello, client", addr)
