# task5

В этой документации представлен краткий обзор HTTP-сервера, написанного на Python с использованием соксетов. Сервер обрабатывает GET и POST запросы от клиентов, предоставляя страницу с оценками и позволяя клиентам добавлять новые оценки.

## HTTP-Сервер (server.py)

Этот сервер предоставляет страницу с оценками и позволяет клиентам добавлять новые оценки. Он прослушивает входящие соединения и анализирует HTTP-запросы от клиентов.

```python
import socket

# Класс MyHTTPServer представляет HTTP-сервер.
class MyHTTPServer:
    def __init__(self, server_ip, server_port, num_listen=1):
        # Создаем сокет и настраиваем его параметры.
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.conn.bind((server_ip, server_port))  # Привязываем сокет к указанному IP и порту.
        self.conn.listen(num_listen)  # Начинаем слушать входящие соединения.
        self.grades = {}  # Словарь для хранения оценок.

    # Основной цикл сервера для обслуживания клиентов.
    def serve_forever(self):
        while True:
            client, addr = self.conn.accept()  # Принимаем входящее соединение от клиента.
            self.serve_client(client)

    # Обслуживание клиента.
    def serve_client(self, client):
        data = client.recv(2 * 16384).decode(encoding="utf-8", errors="ignore")  # Получаем данные от клиента.
        self.request_parser(client, data)  # Анализируем запрос.

    # Анализ HTTP-запроса.
    def request_parser(self, client, data):
        lines = data.split("\n")
        method, url, version = lines[0].split()

        # Парсинг параметров запроса в зависимости от метода (GET или POST):
        if method == "GET":
            params = (
                {p.split("=")[0]: p.split("=")[1] for p in url.split("?")[1].split("&")}
                if "?" in url
                else None
            )
        elif method == "POST":
            # В POST-запросе параметры находятся в теле запроса.
            body = data.split("\n")[-1]
            params = {p.split("=")[0]: p.split("=")[1] for p in body.split("&")}
        else:
            params = None

        # Обработка запроса в зависимости от метода.
        self.handle_request(client, method, params)

    # Обработка HTTP-запроса и отправка ответа.
    def handle_request(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.grades_to_html())  # Отправляем HTML-страницу с оценками.
        elif method == "POST":
            discipline = params.get("discipline")
            grade = params.get("grade")
            self.grades[discipline] = grade  # Сохраняем новую оценку.
            self.send_response(client, 200, "OK",
                               "Содержимое сохранено!")  # Отправляем сообщение об успешном сохранении.
        else:
            self.send_response(client, 404, "Not Found", "Некорректный метод, попробуйте снова.")  # Отправляем ошибку.

    # Отправка HTTP-ответа клиенту.
    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    # Генерация HTML-страницы на основе данных о оценках.
    def grades_to_html(self):
        page = (
            f"<html><body><ul>"
            f"{''.join([f'<li>{discipline}: {grade}' for discipline, grade in self.grades.items()])}"
            f"</ul></body></html>"
        )
        return page

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 7026
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()  # Запуск сервера для бесконечного обслуживания клиентов.
    except KeyboardInterrupt:
        server.conn.close()  # Закрытие серверного соединения при завершении программы.
```

Этот сервер предоставляет страницу с оценками, обрабатывает POST-запросы для добавления оценок и отправляет ответы клиентам. Каждый клиент, подключившийся к серверу, может просматривать оценки и добавлять новые.