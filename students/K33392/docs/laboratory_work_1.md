# Лабораторная работа 1

## Задание 1

### Описание
В данном задании было необходимо реализовать клиентскую и серверную часть приложения. 
Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

### Решение

**Серверная часть**

Для начала нам необходимо импортировать библиотеку для работы с сокетами
и открыть новый сокет. 
В качестве аргументов мы передаем параметры:

* socket.AF INET - IPv4 сокет
* socket.SOCKDGRAM - UDP


```python
import socket

# Create a new socket object
# AF_INET - IPv4 address family
# SOCK_DGRAM - UDP socket type
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Затем нам необходимо привязать сокет к локальному адресу

```python
# Store server address
server_addr = ("localhost", 9090)

# Bind a socket to a local address
sock.bind(server_addr)
```

Для получения данных и ip-адреса используем функцию `recvfrom`
```python
# Receive data and ip address from a client
data, client_addr = sock.recvfrom(1024)
print(data.decode())
```

Для отправки данных клиенту воспользуемся функцией `sendto`

```python
# Send a response to the client
sock.sendto(b"Hello, Client!", client_addr)
```

**Клиентская часть**

Для начала нам необходимо импортировать библиотеку для работы с сокетами
и открыть новый сокет. 
В качестве аргументов мы передаем параметры:

* socket.AF INET - IPv4 сокет
* socket.SOCKDGRAM - UDP

```python
import socket

# Create a new socket object
# AF_INET - IPv4 address family
# SOCK_DGRAM - UDP socket type
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Store server address
server_addr = ("localhost", 9090)
```

Затем отсылаем данные серверу при помощи команды `sendto`
```python
# Send bytes to the server address
sock.sendto(b"Hello, Server!", server_addr)
```

После этого ожидаем ответ от сервера и печатаем его на экран
```python
# Wait for server reply
data = sock.recv(1024)

# Print received data
print(data.decode())
```

## Задание 2

### Описание
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту.

### Решение
**Серверная часть**

Открываем TCP сокет

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(1)
```

Ожидаем подключение к серверу и отсылаем клиенту подсказку о том, 
что ожидает получить сервер в ответном сообщении

```python
conn, addr = sock.accept()
print("Received new connection from", addr)

conn.send(b"Enter a and b splitted by the space, for example: 10 20")
```

Получаем данные, вычисляем сторону по теореме пифагора и отправляем результат клиенту
```python
data = conn.recv(1024)

a, b = list(map(int, data.decode().split()))
result = (a**2 + b**2)**0.5

conn.sendall(str(result).encode())
conn.close()
```

**Клиентская часть**

Открываем TCP сокет и подключаемся к серверу
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 9090)

sock.connect(addr)
```

Получем приветственное сообщение от севера
```python
hello_msg = sock.recv(1024).decode()
print(hello_msg)
```

Запрашиваем данные от пользователя из стандартного ввода, отправляем данные 
на сервер и получаем ответ
```python
data = input().encode()
sock.send(data)
print(sock.recv(1024).decode())
```

## Задание 3

### Описание
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

### Решение

**Серверная часть**

Создадим функцию, которая будет создавать простой HTTP ответ
```python
def create_http_response(body: str) -> bytes:
    request = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {len(body)}\n\n{body}"
    return request.encode()
```

Затем создадим новый сокет, но на этот раз уже TCP (socket.SOCK_STREAM)

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(1)
```

Дальше мы ожидаем подключение к нашему серверу и принимаем его при помощи функции `accept`.
В данном случае мы используем `accept`, так как работаем с TCP сокетом и ожидаем подключение

```python
conn, addr = sock.accept()
```

Затем создаем HTTP запрос с контентом файла `index.html` и отправляем данные клиенту
```python
conn.sendall(create_http_response(open("index.html").read()))
conn.close()
```

**Клиентская часть**

Определим функцию для считывания всех данных из сокета и парсинга тела HTTP-запроса
```python
def socket_read_all(s: socket.socket, chunk_size=1024) -> bytes:
    result = b""
    while (chunk := s.recv(chunk_size)) != b"":
        result += chunk
    return result

def read_http_body(response: bytes) -> str:
    lines = response.decode().splitlines()
    body_start = next((i for i, line in enumerate(lines) if line == ""), -1)
    if body_start == -1:
        raise ValueError("invalid http response")
    return "\n".join(lines[body_start + 1:])
```

После этого создаем сокет, выполняем подключение к серверу, считываем все данные от сервера и печатаем ответа на экран
```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

data = socket_read_all(sock)
body = read_http_body(data)

print(body)
```

## Задание 4

### Описание
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

### Решение

**Протокол для отправки сообщений**

Каждое сообщение состоит из заголовка - 4 байт big-endian, описывающие длину сообщения. Остальные 
N байт - сообщение. Ниже описаны функции создания и получения сообщения
```python
def recv_msg(conn: socket.socket) -> tuple[bytes, bytes]:
    msg_header = conn.recv(4)
    if msg_header == b"":
        return
    length = struct.unpack(">I", msg_header)[0]
    return conn.recv(length)


def create_msg(msg: str):
    msg = msg.encode()
    return struct.pack(">I", len(msg)) + msg
```

**Серверная часть**
Для начала откроем TCP сокет и создадим список для хранения активных подключений.

```python
HOST = "localhost"
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(os.cpu_count())
connections: list[socket.socket] = []
```

Затем начинаем ожидать новые подключения к нашему серверу.
После успешного подключения отправляем клиенту привественное сообщение, добавляем его 
в список активных клиентов и создаем для обработки его запросов отдельный поток. 
```python
def handle_connections(sock: socket.socket):
    print("Server listening on", HOST, "port", PORT)

    while True:
        # Accept client connections
        conn, addr = sock.accept()
        print("New connection", addr)

        conn.send(WELCOME_MESSAGE)

        send_message_to_clients(f"New user has joined: {addr}".encode(), ("Server", ""))

        connections.append((conn, addr))

        # Create a new thread to handle the client
        client_thread = threading.Thread(
            target=handle_client,
            args=(
                conn,
                addr,
            ),
        )
        client_thread.start()
```

Функция для обработки сообщений пользователя ждет сообщения от него, а также отключает клиента
при получении сообщения *"quit"*

```python
def handle_client(conn: socket.socket, addr: tuple):
    try:
        while (msg := recv_msg(conn)) is not None and msg != b"quit":
            send_message_to_clients(msg, addr)
    finally:
        conn.close()
```

Также определена функция, которая отправляет сообщение всем клиентам данного чата
и удаляет неиспользуемые подключения

```python
def send_message_to_clients(msg: bytes, addr: tuple):
    global connections

    payload = create_msg(f"{addr[0]}:{addr[1]}: ".encode() + msg + b"\n")

    # Send message to all connected users
    indexes = set()
    for i, (conn, conn_addr) in enumerate(connections):
        if addr == conn_addr:
            continue
        try:
            conn.send(payload)
        except OSError:
            indexes.add(i)

    # Remove disconnected users
    indexes = list(indexes)
    indexes.reverse()
    for i in indexes:
        connections.pop(i)
```

**Клиентская часть**

Для начала коммуникации в чате создаем сокет, подключаемся к серверу и ждем сообщения
из стандартного ввода от пользователя. Также мы создаем отдельный поток для обработки сообщений от сервера, так как иначе стандартный ввод будет блокировать получение сообщений
```python
# Init socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((HOST, PORT))

# Create thread for handling servers' messages
t = threading.Thread(target=handle_messages, args=(sock,))
t.start()

while True:
    try:
        # Get users' input and send it to the server
        sock.sendall(create_msg(input(INPUT_PROMPT)))
    except OSError:
        break
```

Функция по обработке сообщений с сервера получает сообщения в нашем формате и закрывает сокет,
если мы получили пустой ответ от сервера

```python
def handle_messages(conn: socket.socket):
    while (msg := recv_msg(conn)) is not None and msg != b"":
        print(f"\n{msg.decode()}\n{INPUT_PROMPT}", end="")
    sock.close()
    print("LEAVING")
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

Создадим классы для хранения данных о запросах, ответах и HTTP методах
```python
class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class HTTPRequest:
    method: HTTPMethod
    protocol: str
    path: str
    headers: dict[str, str]
    body: bytes


@dataclass
class HTTPResponse:
    status: int
    headers: dict[str, str]
    body: bytes
    protocol: str = "HTTP/1.1"

    def __bytes__(self):
        headers_str = "\n".join(f"{key}: {val}" for key, val in self.headers.items())
        return f"{self.protocol} {self.status} {HTTPStatus(self.status).phrase}\n{headers_str}\n\n".encode() + self.body
```

Хранить наши оценки мы будем в контейнере `defaultdict`
```python
SCORES = defaultdict(list)
```

В нашем классе `HTTPServer` определим функции контекстного менеджера 
```python

def __enter__(self):
    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return self

def __exit__(self, *_):
    logging.info("Shutting down the server")
    self.__socket.close()

```

Определим функцию для парсинга запроса от клиента

```python
def __parse_request(self, conn: socket.socket) -> HTTPRequest:
    f = conn.recv(1024 * 6)
    lines = f.splitlines()

    # Parse start-line
    try:
        method, path, protocol = lines[0].decode().strip().split()
    except IndexError:
        raise Exception("Malformed start-line")

    # Parse headers
    headers: dict[str, str] = {}
    index = 1
    req_generator = ((n, i.decode()) for n, i in enumerate(lines[1:], 1))
    while (data := next(req_generator, None)) is not None and data[1].strip() != "":
        index, header = data
        try:
            key, val = header.split(":")
            headers[key.lower()] = val.strip()
        except ValueError:
            raise Exception("Malformed headers")

    # Parse body
    body = b"".join(lines[index + 2 :])
    return HTTPRequest(HTTPMethod(method), protocol, path, headers, body)
```

Логика по обработке запроса достаточно проста

1. Парсим запрос от клиента
2. Обрабатываем запрос и создаем ответ
3. Отправляем ответ клиенту


```python
def __handle_client(self, conn: socket.socket):
    req = self.__parse_request(conn)
    resp = self.__handle_request(req)
    self.__send_response(conn, resp)

def __send_response(self, conn: socket.socket, resp: HTTPResponse):
    logging.info(f"Sent {conn.send(bytes(resp))} bytes")
```

Функция для обработки запроса выглядит так

```python
def __handle_request(self, req: HTTPRequest):
    logging.info(f"Got {req.method} request {req.path}")
    if req.method == HTTPMethod.GET and req.path.startswith("/scores"):
        query_params = parse_qs(urlparse(req.path).query)
        if "subject" not in query_params:
            return HTTPResponse(
                status=400,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"detail": "subject query param was not specified"}).encode(),
            )
        return HTTPResponse(
            status=200,
            headers={"Content-Type": "application/json"},
            body=json.dumps({"score": SCORES[query_params["subject"][0]]}).encode(),
        )
    elif req.method == HTTPMethod.POST and req.path.startswith("/subject"):
        query_params = parse_qs(urlparse(req.path).query)
        if "name" not in query_params:
            return HTTPResponse(
                status=400,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"detail": "name query param was not specified"}).encode(),
            )
        if "score" not in query_params:
            return HTTPResponse(
                status=400,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"detail": "score query param was not specified"}).encode(),
            )
        SCORES[query_params["name"][0]].append(query_params["score"][0])
        return HTTPResponse(status=200, headers={}, body=b"")
    return HTTPResponse(status=404, headers={}, body=b"")
```

**Клиентская часть**

GET запрос

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))
sock.send(b"GET /scores?subject=test HTTP/1.1\nContent-Type: text")
print(sock.recv(1024 * 4).decode())
```

POST запрос
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))
sock.send(b"POST /subject?name=test&score=10 HTTP/1.1\nContent-Type: text")
print(sock.recv(1024 * 4).decode())
```