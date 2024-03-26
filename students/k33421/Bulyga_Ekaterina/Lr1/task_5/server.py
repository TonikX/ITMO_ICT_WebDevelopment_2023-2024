import socket


class MyHTTPServer:
    with open('index.html', 'r', encoding='utf-8') as file:
        base = file.read()
    with open('form.html', 'r', encoding='utf-8') as file:
        form = file.read()
    with open('table.html', 'r', encoding='utf-8') as file:
        table = file.read()

    # Параметры сервера
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.body = self.page()

    def serve_forever(self):
        # 1. Запуск сервера на сокете, обработка входящих соединений
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print(f"Serving HTTP on {self.host} port {self.port}...")
            while True:
                client_connection, client_address = server_socket.accept()
                self.serve_client(client_connection)
        finally:
            server_socket.close()

    def serve_client(self, client_connection):
        # 2. Обработка клиентского подключения
        request = client_connection.recv(1024)
        request_lines = request.split(b"\r\n")
        method, url, protocol = self.parse_request(request_lines[0])
        other_headers = self.parse_headers(request_lines[1:])

        if url != b'/favicon.ico':
            if method == b'GET':
                self.handle_request(method, url)
            else:
                self.handle_request(method, url, request_lines[-1])
            self.send_response(client_connection, '200', 'OK', other_headers)

    def parse_request(self, header):
        # 3. функция для обработки заголовка http+запроса. Python, сокет предоставляет возможность создать вокруг него некоторую обертку, которая предоставляет file object интерфейс. Это дайте возможность построчно обработать запрос. Заголовок всегда - первая строка. Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола). URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143 , где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
        method, url, protocol = header.split()
        return method, url, protocol

    def parse_headers(self, headers):
        # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
        return [header for header in headers if header != b'']

    def page(self, filters=None):
        text = ''
        with open('ratings.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                values = line.split(',')
                if values:
                    if filters is not None:
                        if 'option1' in filters and filters['option1'] == values[1] and \
                                'option2' in filters and filters['option2'] == values[3] or \
                                'option1' in filters and filters['option1'] == values[1] or \
                                'option2' in filters and filters['option2'] == values[3]:
                            text += f'<tr><td>{values[1]}</td><td>{values[3]}</td></tr>'
                    else:
                        text += f'<tr><td>{values[1]}</td><td>{values[3]}</td></tr>'
        return MyHTTPServer.base.format(MyHTTPServer.form, MyHTTPServer.table.format(text))

    def handle_request(self, method, url, request=None):
        # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор условий, который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
        if method == b'GET':
            if url != b'/':
                params = {item.split('=')[0]: item.split('=')[1] for item in url[2:].decode('utf-8').split("&")}
                self.body = self.page(params)
            else:
                self.body = self.page()
        else:
            params = {item.split('=')[0]: item.split('=')[1] for item in request[2:].decode('utf-8').split("&")}
            with open('ratings.txt', 'a', encoding='utf-8') as file:
                print(*[f'{key},{value}' for key, value in params.items()], sep=',', file=file)
            self.body = self.page()

    def send_response(self, client_connection, status_code, reason, headers=None):
        # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
        response = f"HTTP/1.1 {status_code} {reason}\r\n"

        # Запись заголовков в ответ
        if headers:
            for header in headers:
                response += f"{str(header)}\r\n"

        # Добавление пустой строки для обозначения конца секции заголовков
        response += "\r\n"

        response += self.body

        # Отправка ответа клиенту
        client_connection.sendall(response.encode())
        client_connection.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5555
    name = 'test'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
