# Лабораторная работа 1: работа с сокетами

### Дисциплина: основы web-программирования

**Цель**: Овладеть практическими навыками и умениями реализации web-серверов и
использования сокетов.

**Оборудование**: компьютерный класс.
**Программное обеспечение**: Python 2.7-3.6, библиотеки Python: sys, socket.

# Практическое задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

- Обязательно использовать библиотеку socket

- Реализовать с помощью протокола UDP

### Сервер

###### Импорты и глобальные переменные

```
    import socket
    import threading

    PORT = 8080
```

###### Тело сервера

```
    def main():

        global PORT

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', PORT))

        while True:
            data, addr = sock.recvfrom(1024)
            thread = threading.Thread(target=recieve, args=([data, addr, sock],))
            thread.start()
```

###### Функция обработки подключения

```
    def recieve(data):
        print(data[0])
        data[2].sendto(b"Hello, client", data[1])

```

### Клиент

###### Импорты и глобальные переменные

```
    import socket

    PORT = 8080
```

###### Тело клиента

```
    def main():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'Hello, server', ('localhost', PORT))
        data, addr = sock.recvfrom(1024)
        print(data)
```

# Практическое задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Варианты:

- a. Теорема Пифагора
- **b. Решение квадратного уравнения.**
- c. Поиск площади трапеции.
- d. Поиск площади параллелограмма.

Обязательно использовать библиотеку socket
Реализовать с помощью протокола TCP

### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело сервера

```
def main():

    PORT = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(10)

    while True:

        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=([client_socket, client_address], ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break
```

###### Обработка подключения

```
def parce_string(string):
    return string.split()

def chat(client):

    while True:
        client_socket = client[0]
        client_address = client[1]

        data = client_socket.recv(65536).decode('utf-8')
        a, b, c = parce_string(data)
        x1, x2 = quadratic_equation(int(a), int(b), int(c))
        ans = f"X1= {x1}, X2= {x2}"
        client_socket.sendto(ans.encode(), client_address)
```

###### Расчет ответа

```
def quadratic_equation(a, b, c):

    x1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)
    return x1, x2

```

### Клиент

###### Импорты и глобальные переменные

```
import socket
import threading
import time

PORT = 8080
```

###### Тело клиента

```
def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()
```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        client_socket.sendall(f'{random.randint(-100, 100)} {random.randint(-100, 100)} {random.randint(-100, 100)}'
                              .encode('utf-8'))
        time.sleep(1)
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        ans = client_socket.recv(1024).decode('utf-8')
        print(ans)
```

# Практическое задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

**Полезные ссылки:**

- http://zetcode.com/python/socket/

Обязательно использовать библиотеку socket

### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело сервера

```
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=(client_socket, ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break
```

###### Обработка подключения

```
def chat(client_socket):
    while True:
        client_socket.recv(1000)
        response_type = 'HTTP/1.0 200 OK\n'
        headers = 'Content-Type: text/html\n\n'
        with open('index.html', 'r') as f:
            body = f.read()

        response = response_type + headers + body
        client_socket.send(response.encode('utf-8'))
```

### Клиент

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело клиента

```
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()

```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        client_socket.send(b"GET / HTTP/1.0\r\nHost:localhost\r\n\r\n")
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
```

# Практическое задание 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.
Обязательно использовать библиотеку

Реализовать с помощью протокола TCP – 100% баллов, с помощью UDP – 80%.

Обязательно использовать библиотеку threading.

Для реализации с помощью UDP, thearding использовать для получения
сообщений у клиента.

Для применения с TCP необходимо запускать клиентские подключения И прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.

### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
clients = {}
```

###### Тело сервера

```
def main():

    global PORT
    global clients

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    while True:
        client_socket, (client_host, client_port) = server_socket.accept()
        client_socket.send(b'Enter your nickname: ')
        nick = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = nick
        thread = threading.Thread(target=chat, args=(client_socket,))
        thread.start()
```

###### Обработка сообщений от клиентов

```
def chat(client_socket):
    global clients

    while True:
        mail = client_socket.recv(1024).decode('utf-8')
        for sock in clients.keys():
            sock.send(f'{clients[client_socket]} send: {mail}'.encode('utf-8'))

```

### Клиент

###### Импорты и глобальные переменные

```
import socket
import threading

PORT = 8080
```

###### Тело клиента

```
def main():

    global PORT

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))
    message = client_socket.recv(4096)
    print(message.decode())
    nick = input()
    client_socket.send(nick.encode('utf-8'))
    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()
```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
```

# Практическое задание 4

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:

- Принять и записать информацию о дисциплине и оценке по дисциплине.
- Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

### Сервер

###### Импорты и глобальные переменные

```
import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import urlparse
from urllib.parse import parse_qs

MAX_LINE = 64*1024

```

###### Запуск сервера

```
if __name__ == '__main__':
    host = 'localhost'
    port = 5321
    name = "name"

    serv = MyHTTPServer(host=host, port=port, name=name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

###### Тело сервера

```
class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.journal = {}

    def serve_forever(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(10)

            while True:
                client_socket, (client_host, client_port) = server_socket.accept()
                try:
                    self.serve_client(client_socket)
                except Exception as e:
                    print('Client serving failed', e)
                print(client_socket)
                client_socket.close()
        finally:
            server_socket.close()

    def serve_client(self, client_socket):
        try:
            request = self.parse_request(client_socket)
            response = self.handle_request(request)
            self.send_response(client_socket, response)
        except ConnectionResetError:
            client_socket = None
        except Exception as e:
            self.send_error(client_socket, e)

        if client_socket:
            client_socket.close()

    def parse_request(self, client_socket):
        rfile = client_socket.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)

        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')

        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')
            if line in (b'\r\n', b'\n', b''):
                break
            headers.append(line)

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)  # эффективно читаем строку целиком
        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        headers_words = req_line.split()  # разделяем по пробелу

        if len(headers_words) != 3:  # и ожидаем ровно 3 части
            raise Exception('Malformed request line')

        method, target, ver = headers_words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        return method, target, ver

    def handle_request(self, req):
        if req.path == '/journal/add' and req.method == 'POST':
            return self.handle_post_mark(req)

        if req.path == '/journal' and req.method == 'GET':
            return self.handle_get_subject(req)

        raise Exception('Not found')

    def handle_post_mark(self, req):
        subj = req.query['subject'][0]
        mark = req.query['mark'][0]

        if subj in self.journal.keys():
            mark_id = len(self.journal[subj])+1
        else:
            self.journal[subj] = []
            mark_id = 1
        self.journal[subj].append({'id': mark_id, 'grade': mark})
        return Response(204, 'Created')

    def handle_get_subject(self, req):
        contentType = 'text/html; charset=utf-8'
        body = '<html><head>Журнал</head><body>'

        for subj in self.journal:
            body += f'<div>Оценки по предмету: ({subj})</div>'
            body += '<ul>'
            for u in self.journal[subj]:
                body += f'<li>#{u["id"]}: {u["grade"]}</li>'
                body += '</ul>'

        body += '</body></html>'
        body = body.encode('utf-8')

        headers = [('Content-Type', contentType),
                   ('Content-Length', len(body))]

        print(headers)
        return Response(200, 'OK', headers, body)


    def send_response(self, client_socket, resp):
        wfile = client_socket.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()


    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
        resp = Response(status, reason,
                        [('Content-Length', len(body))],
                        body)
        self.send_response(conn, resp)

```

###### Вспомогательные классы

```
class HTTPError(Exception):
  def __init__(self, status, reason, body=None):
    super()
    self.status = status
    self.reason = reason
    self.body = body


class Response:
  def __init__(self, status, reason, headers=None, body=None):
    self.status = status
    self.reason = reason
    self.headers = headers
    self.body = body


class Request:
  def __init__(self, method, target, version, headers, rfile):
    self.method = method
    self.target = target
    self.version = version
    self.headers = headers
    self.rfile = rfile

  @property
  def path(self):
    return self.url.path

  @property
  @lru_cache(maxsize=None)
  def query(self):
    return parse_qs(self.url.query)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)

  def body(self):
    size = self.headers.get('Content-Length')
    if not size:
      return None
    return self.rfile.read(size)
```

### Клиент

###### Импорты и глобальные переменные

```
import socket

PORT = 5321
```

###### Тело клиента

```
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', PORT))
    client_socket.send(b"POST /journal/add?subject=Maths&mark=4 HTTP/1.1\r\nHost:www.example.com\r\nAccept:text/html\r\n\r\n")
    #client_socket.send(b"GET /journal/subject?subject=Maths HTTP/1.1\r\nHost:www.example.com\r\nAccept:text/html\r\n\r\n")
    response = client_socket.recv(4096)
    client_socket.close()
    print(response.decode())
```
