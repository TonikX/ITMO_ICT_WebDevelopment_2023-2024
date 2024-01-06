import socket

if __name__ == "__main__":
    # Загружаем содержимое файла "index.html".
    content = open("index.html").read()

    # Задаем IP-адрес и порт сервера, на котором будем слушать входящие соединения.
    server_ip = "127.0.0.1"
    server_port = 7002

    # Создаем TCP сокет (SOCK_STREAM), связываем его с указанным IP-адресом и портом, и начинаем слушать входящие соединения.
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((server_ip, server_port))
    conn.listen()

    while True:
        # Принимаем входящее соединение и получаем сокет клиента.
        client_socket = conn.accept()[0]

        # Получаем данные от клиента.
        data = client_socket.recv(1024)

        # Создаем HTTP-ответ с кодом 200 OK и вставляем содержимое "index.html" в ответ.
        response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content

        # Отправляем ответ клиенту.
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом.
        client_socket.close()



