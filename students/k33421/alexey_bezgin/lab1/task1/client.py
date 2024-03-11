import socket

if __name__ == "__main__":
    # Задаем IP-адрес и порт сервера, к которому мы хотим подключиться.
    server_ip = '127.0.0.1'
    server_port = 7000

    # Создаем UDP сокет (SOCK_DGRAM) и устанавливаем соединение с сервером.
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.connect((server_ip, server_port))

    # Отправляем сообщение "Hello, server" серверу.
    conn.send(b"Hello, server")

    # Получаем данные от сервера и адрес, с которого пришли данные.
    data, addr = conn.recvfrom(1024)

    # Выводим полученные данные (раскодированные из байтовой строки) на экран.
    print(data.decode("utf-8"))


