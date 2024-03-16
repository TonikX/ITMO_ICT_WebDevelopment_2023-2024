# Лабораторная работа 1

## Задание 1

### Описание

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку `socket`
Реализовать с помощью протокола `UDP`

### Решение

**Server**

В файл server.py импортируем дефолтную библиотеку socket

Далее передаем ей следующие параметры для создания сокета:

* socket.AF_INET - IPv4 сокет
* socket.SOCKDGRAM - UDP протокол

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Далее завязываемся на нашем локальном адресе

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _socket.bind(("localhost", 9090))
```

Для получения данных и ip-адреса используем `recvfrom`, которой передаем размер буфера

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _socket.bind(("localhost", 9090))
    print("socket bound, wait messages...")
    while True:
        data, client_address = _socket.recvfrom(1024)

```

Для отправки просто используем `sendto`

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _socket.bind(("localhost", 9090))
    print("socket bound, wait messages...")
    while True:
        data, client_address = _socket.recvfrom(1024)
        parsed_data = data.decode()
        print(f"Message from client: {parsed_data}")

        response = b"Hello, client"
        _socket.sendto(response, client_address)

```

**Client**

В файл client.py импортируем дефолтную библиотеку socket

Далее передаем ей следующие параметры для создания сокета:

* socket.AF_INET - IPv4 сокет
* socket.SOCKDGRAM - UDP протокол

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

```

Заполняем адрес сервера и отсылаем данные с помощью `sendto`

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ("localhost", 9090)

    message = b"Hello, server"

    try:
        _socket.sendto(message, server_address)
    finally:
        _socket.close()

```

После этого ожидаем ответ и выводим его

```python
import socket


def init_socket():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ("localhost", 9090)

    message = b"Hello, server"

    try:
        _socket.sendto(message, server_address)
        data = _socket.recv(1024)
        print(f"Server answered: {data.decode()}")

    finally:
        _socket.close()


if __name__ == '__main__':
    init_socket()

```

## Задание 2

### Описание

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту.

Вариант: Теорема Пифагора

### Решение

**Серверная часть**

Открываем TCP сокет через SOCK_STREAM
Также устанавливаем очередь на подключение в единицу

```python
import socket


def init_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    _socket.bind(server_address)

    _socket.listen(1)
```

Ожидаем подключение к серверу

```python
def init_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    _socket.bind(server_address)

    _socket.listen(1)
    print("Wait client...")
    client_socket, client_address = _socket.accept()
    print(f"Client connected: {client_address}")
```

Получаем данные, вычисляем сторону по теореме пифагора и отправляем результат клиенту

```python
def init_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    _socket.bind(server_address)

    _socket.listen(1)
    print("Wait client...")
    client_socket, client_address = _socket.accept()
    print(f"Client connected: {client_address}")

    while True:
        try:
            data = client_socket.recv(1024)
            params = eval(data.decode("utf-8"))
            if len(params) == 2:
                first_cathetus, second_cathetus = map(float, params)
                result = calculate_pythagoras(first_cathetus, second_cathetus)
                client_socket.send(str(result).encode("utf-8"))
            else:
                client_socket.send("Check your data, server receive only two args".encode("utf-8"))
        except Exception as e:
            client_socket.send(f"ERROR: {str(e)}".encode("utf-8"))
            print(f"ERROR: {str(e)}")
            break

    client_socket.close()
    _socket.close()
```

Сама функция вычисления:

```python
def calculate_pythagoras(first_cathetus, second_cathetus):
    return math.sqrt(first_cathetus ** 2 + second_cathetus ** 2)
```

**Клиентская часть**

Открываем TCP сокет, подключаемся к серверу

```python
import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    client_socket.connect(server_address)

```

Запрашиваем данные от пользователя из стандартного ввода, отправляем данные
на сервер и получаем ответ

```python
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    client_socket.connect(server_address)

    first_cathetus = float(input("Введите длину первого катета: "))
    second_cathetus = float(input("Введите длину второго катета: "))

    data = str([first_cathetus, second_cathetus]).encode("utf-8")
    client_socket.send(data)

    result = client_socket.recv(1024).decode("utf-8")
    print(f"гипотенуза в прямоугольном треугольнике: {result}")

    client_socket.close()
```

## Задание 3

### Описание

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

### Решение

**Серверная часть**

Для начала создадим функцию, которая возвращает готовый response

```python
def generate_http_response():
    html_content = open('index.html', 'r', encoding='utf-8').read()

    http_header = "HTTP/1.1 200 OK\r\n"
    http_header += "Content-Type: text/html; charset=UTF-8\r\n"
    http_header += f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
    http_header += "\r\n"
    http_response = http_header + html_content
    return http_response
```

Создаем TCP сокет(SOCK_STREAM), подключаемся

```python
def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9090)
    server_socket.bind(server_address)
    server_socket.listen(1)
```

Дальше мы ожидаем подключение к нашему серверу и принимаем его при помощи функции `accept`.
Используем именно эту функцию, так как работаем с TCP сокетом и ожидаем подключения

```python
def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9090)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("wait client...")
    client, client_address = server_socket.accept()
    print(f"Connected client: {client_address}")
```

Затем отправляем данные клиенту

```python
def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9090)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("wait client...")
    client, client_address = server_socket.accept()
    print(f"Connected client: {client_address}")
    while True:
        try:
            if client.recv(1024) is not None:
                http_response = generate_http_response()
                client.send(http_response.encode('utf-8'))
                client.close()
            break
        except Exception as e:
            print(f"ERROR: {str(e)}")
            client.send(str(e).encode("utf-8"))
            break

    server_socket.close()
```

## Задание 4

### Описание

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

### Решение

**Протокол для отправки сообщений**

**Серверная часть**
Создадим класс ChatServer, в котором будет храниться вся логика многопользовательского чата

```python
class ChatServer:
    _socket: socket # <- сокет, в единственном экземпляре на каждый сервер
    _connections: list[socket.socket] = [] # <- список всех наших юзеров

```
Далее делаем функцию инициализации, в которой будут выполнены все настройки и запуск сервера
```python
    def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # <- протокол TCP
        self._socket.bind(("localhost", 9090))
        print("server started")
        self._socket.listen(4) # <- не даем подключаться к чату больше, чем 4ым людям
        self.handle_connections(self._socket) # <- уходим в цикл, в котором будем дальше управлять подключениями и сообщениями
```

Затем начинаем ожидать подключения к нашему серверу.
После успешного подключения отправляем клиенту привественное сообщение, добавляем его
в список юзеров и создаем новый поток для обработки его сообщений.

```python
    def handle_connections(self, sock: socket.socket):
    print("server handle connections")
    while True:
        connection, address = sock.accept()
        print(f"Client connected: {address}")

        connection.send("Welcome to chat!".encode("utf-8")) #<- отправка сообщения пользователю

        self.send_message_to_clients(f"New user joined: {address}".encode("utf-8"), ("server side", "")) #<- отправка сообщения пользователю

        self._connections.append((connection, address)) #<- сохраняем нашего юзера в списке подключений

        client_thread = threading.Thread(
            target=self.handle_client_message,
            args=(
                connection,
                address,
            ),
        )
        client_thread.start()
```

Функция для обработки сообщений пользователя ждет сообщения и отправляет его другим пользователям

```python
    def handle_client_message(self, connection: socket.socket, user_address: tuple):
        try:
            previous_message = b""
            while True:
                message = connection.recv(1024)
                if message != b"" and message != previous_message:
                    previous_message = message
                    self.send_message_to_clients(message, user_address)
                if message == b"Quit":
                    break
        finally:
            connection.close()
```

Собственно функция отправки сообщения другим

```python
    def send_message_to_clients(self, message: bytes, address: tuple):

        message = (f"{address[0]}:".encode("utf-8") + message + b"\n")

        # Нужно отправить всем подключением сообщение, исключая пользователя
        unreceived_users = set()
        for index, (connection, connectionAddress) in enumerate(self._connections):
            if address != connectionAddress:
                try:
                    connection.send(message)
                except OSError:
                    unreceived_users.add(index)

        unreceived_users = list(unreceived_users) 
        for index in unreceived_users:
            self._connections.pop(index) #<- если пользаки не получили сообщения, то они не на сервере, убираем их
```

**Клиентская часть**

Создаем сокет, подключаемся к серверу и ждем сообщения
из консоли. Также мы создаем отдельный поток для обработки сообщений от сервера и отправки сообщений на сервер,
т.к. main поток не должен делать это (возникнет блокировка)

```python
import socket
import threading
if __name__ == "__main__":
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.connect(("localhost", 9090))

    handleThread = threading.Thread(target=handle_messages, args=[_socket], name="Handle thread")
    handleThread.start()
    sendToChatThread = threading.Thread(target=send_to_chat, args=[_socket], name="Send to chat thread")

```

Функция по обработке сообщений с сервера получает сообщения и выводит пользователю

```python
import socket


def handle_messages(connection: socket.socket):
    while True:
        message = connection.recv(1024)
        if message is not None and message != b"":
            print(message.decode("utf-8"))
```
Полный код

```python
import socket
import threading


def handle_messages(connection: socket.socket):
    while True:
        message = connection.recv(1024)
        if message is not None and message != b"":
            print(message.decode("utf-8"))


def send_to_chat(connection: socket.socket):
    while True:
        try:
            message = input("Введите ваше сообщение")
            if message != "Quit":
                connection.send(message.encode("utf-8"))
            else:
                connection.send(message.encode("utf-8"))
                print("Bye")
                connection.close()
        except OSError:
            break


if __name__ == "__main__":
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.connect(("localhost", 9090))

    handleThread = threading.Thread(target=handle_messages, args=[_socket], name="Handle thread")
    handleThread.start()
    sendToChatThread = threading.Thread(target=send_to_chat, args=[_socket], name="Send to chat thread")

```
## Задание 5

### Описание

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:

* Принять и записать информацию о дисциплине и оценке по дисциплине.
* Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

### Решение

**Серверная часть**

Создадим DTOшки 

```python
class Method(Enum):
    GET = 'GET'
    POST = 'POST'

# @see https://developer.mozilla.org/ru/docs/Web/HTTP/Overview#http_%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F
@dataclass
class Request:
    method: Method
    path: str
    protocolVersion: str
    headers: dict[str, str]
    body: bytes


# @see https://developer.mozilla.org/ru/docs/Web/HTTP/Overview#http_%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F
@dataclass
class Response:
    protocolVersion: str
    headers: dict[str, str]
    body: bytes
    status: int

    def to_byte(self): # <- поскольку мы делаем это без библиотек, то будем преобразовывать response сами в байты
        headers_str = "\n".join(f"{header_key}: {header_value}" for header_key, header_value in self.headers.items())
        return f"{self.protocolVersion} {self.status} {HTTPStatus(self.status).phrase}\n{headers_str}\n\n".encode() + self.body
```

Создадим класс MyHTTPServer в котором будут храниться оценки, а также содержаться вся бизнес-логика

```python
class MyHTTPServer:
    _socket: socket.socket
    _grades: dict[str, int] = dict()

    def __init__(self, host, port):
        self._host = host
        self._port = port
```

Далее создаем функцию init(), которая будет отвечать за старт сервера

```python

    def init(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen(1)
        print(f"server started in {self._host}:{self._port}")
        while True:
            client = self._socket.accept()
            try:
                response = self.handle_client_request(client[0])
                self.send_response(response, client[0])
            except Exception as error:
                print(f"{error}")

```

Парсим запрос от пользователя

```python
    def map_to_request_model(self, client: socket.socket) -> Request:
        data = client.recv(2048).splitlines()
        method, path, protocol_ver = data[0].decode().strip().split()
        headers, last_header_index = self.parse_headers(data[1:]) #<- игнорим строку, которую прочли
        body = b"".join(data[last_header_index + 2:]) #<- от последнего хэдера отсутпаем через ненужные строки и забираем body

        return Request(Method(method), path, protocol_ver, headers, body)
```

Парсер хэдера тоже просто делается
```python
    def parse_headers(self, data: list[bytes]) -> tuple[dict[str, str], int]:
        index = -1
        headers: dict[str, str] = dict()
        generator = ((n, i.decode()) for n, i in enumerate(data))
        while (line_data := next(generator, None)) is not None and line_data[1].strip() != "": #<- важно чтобы значение хэдера было не пустым
            index, header = line_data
            try:
                key, value = header.split(":")
                headers[key.lower()] = value.strip()
            except ValueError:
                raise Exception("Wrong header")

        return headers, index
```

Маппинг Request'а в Response делается довольно просто, внутри смотрим на тип и совпадение пути

```python
    def get_response(self, request) -> Response:
        print(f"get_response:{request.method} {request.path}")
        if request.method == Method.GET and request.path.startswith("/grades"):
            query_parameters = parse_qs(urlparse(request.path).query)
            if "subject" not in query_parameters:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "subject query param was not specified"}).encode(),
                )

            return Response(
                protocolVersion="HTTP/1.1",
                status=200,
                headers={"Content-Type": "text/html", "charset": "UTF-8"},
                body=self.generate_html().encode(),
            )
        elif request.method == Method.POST and request.path.startswith("/subject"):
            query_params = parse_qs(urlparse(request.path).query)
            if "name" not in query_params:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "name query param was not specified"}).encode(),
                )
            if "grade" not in query_params:
                return Response(
                    protocolVersion="HTTP/1.1",
                    status=400,
                    headers={"Content-Type": "application/json"},
                    body=json.dumps({"errorMessage": "score query param was not specified"}).encode(),
                )
            self._grades[query_params["name"][0]] = query_params["grade"][0]
            return Response(protocolVersion="HTTP/1.1", status=200, headers={}, body=b"")
        else:
            Response(protocolVersion="HTTP/1.1", status=404, headers={}, body=b"")
```

Функция для отправки буквально занимает одну строку

```python
    def send_response(self, response: Response, client: socket.socket):
        client.send(response.to_byte())
```

**Клиентская часть**

GET запрос

```python
import socket

if __name__ == '__main__':
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect(("localhost", 9090))
    _socket.send(b"GET /grades?subject=web HTTP/1.1\nContent-Type: text")

    answer = _socket.recv(1024 * 2).decode()
    print(answer)

```

POST запрос

```python
import socket

if __name__ == '__main__':
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect(("localhost", 9090))
    _socket.send(b"POST /subject?name=web&grade=5 HTTP/1.1\nContent-Type: application/x-www-form-urlencoded")
    print(_socket.recv(1024 * 2).decode())

```