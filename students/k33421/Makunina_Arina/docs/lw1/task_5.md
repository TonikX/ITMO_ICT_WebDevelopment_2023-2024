# Задание 5: Простой web-сервер для обработки HTTP GET и POST запросов

В рамках данного задания было требование создать простой web-сервер с возможностью обработки HTTP GET и POST запросов. Сервер должен быть реализован с использованием Python и библиотеки socket. Основной функционал сервера включает в себя прием и обработку информации о дисциплине и оценке по этой дисциплине, а также предоставление информации обо всех оценках по дисциплине в виде HTML-страницы.

## Реализация сервера

Для выполнения данной задачи был создан класс `MyHTTPServer`, который представляет собой HTTP-сервер. В этом классе определены следующие методы и атрибуты:

- `__init__(self, host, port)`: Конструктор класса, инициализирует сервер с указанным хостом и портом, создает сокет для прослушивания соединений и инициализирует пустой словарь `grades` для хранения оценок.

- `serve_forever(self)`: Метод для запуска сервера в бесконечном цикле, ожидающем подключения клиентов.

- `serve_client(self, client)`: Метод для обслуживания клиента, получает данные от клиента и передает их на обработку.

- `parse_request(self, client, data)`: Метод для разбора HTTP-запроса от клиента и определения его типа (GET или POST).

- `handle_request(self, client, method, params)`: Метод для обработки HTTP-запроса в зависимости от его типа (GET или POST). Для GET-запроса возвращает HTML-страницу с оценками, а для POST-запроса сохраняет переданные данные об оценке в словаре `grades`.

- `send_response(self, client, code, reason, body)`: Метод для отправки HTTP-ответа клиенту с указанным кодом, причиной и телом ответа.

- `grades_to_html(self)`: Метод для преобразования оценок из словаря в HTML-страницу.

## Примеры запросов

Для тестирования сервера были использованы следующие запросы с использованием `curl`:

1. POST-запрос для добавления оценки по дисциплине "Russian" с оценкой "4":
   ```bash
   >curl -X POST "http://localhost:6660" -H "Content-Type: application/json" -d "{\"discipline\": \"Russian\", \"grade\": \"4\"}"
   ```

2. GET-запрос для получения информации обо всех оценках:
   ```bash
   curl -i -X GET http://localhost:6660
   ```
## Пример кода

Приведён пример кода для серверной части:

```python
import json
import socket
import urllib.parse


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.grades = {}

    def serve_forever(self):
        print(f"Server is listening on http://{self.host}:{self.port}")
        while True:
            client, addr = self.socket.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(16384).decode("utf-8")
        if not data:
            client.close()
            return
        self.parse_request(client, data)

    def parse_request(self, client, data):
        lines = data.split("\n")
        if len(lines) < 1:
            self.send_response(client, 400, "Bad Request", "Invalid request")
            client.close()
            return

        request_line = lines[0].split()
        if len(request_line) != 3:
            self.send_response(client, 400, "Bad Request", "Invalid request line")
            client.close()
            return

        method, url, version = request_line
        parsed_url = urllib.parse.urlparse(url)
        print(data)
        params = data.split("\r\n\r\n")[1]
        self.handle_request(client, method, params)

    def handle_request(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.grades_to_html())
        elif method == "POST":
            params = json.loads(params)
            discipline = params.get("discipline")
            grade = params.get("grade")
            if discipline and grade:
                self.grades[discipline] = grade
                self.send_response(client, 200, "OK", "Saved!")
            else:
                self.send_response(
                    client, 400, "Bad Request", "Discipline and grade are required."
                )
        else:
            self.send_response(client, 404, "Not Found", "Incorrect method.")

    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    def grades_to_html(self):
        grade_list = "".join(
            [f"<li>{discipline}: {grade}" for discipline, grade in self.grades.items()]
        )
        return f"<html><body><ul>{grade_list}</ul></body></html>"


if __name__ == "__main__":
    host = "localhost"
    port = 6660
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

```

Разработанный web-сервер успешно обрабатывает HTTP GET и POST запросы, позволяя добавлять и просматривать информацию об оценках по дисциплинам.