## Задание 1
### Клиентская часть
Устанавливаем сокет клиента по UDP:
```Python
import socket

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))
```
Пакуем и отправляем сообщение, получаем ответ от сервера:
```Python
message = 'Hello server!'
s.sendto(message.encode('utf-8'), (HOST, PORT))

data = s.recv(1024)
print('Received: ' + data.decode('utf-8'))

s.close()
```
### Серверная часть
Устанавливаем сокет сервера по UDP:
```Python
import socket
import sys

HOST = 'localhost'
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
```
Обрабатываем подключение
```Python
while True:

    data, addr = s.recvfrom(1024)
    print('Received: ' + data.decode('utf-8'))

    message = 'Hello, client!'
    s.sendto(message.encode('utf-8'), addr)
```
## Задание 2
Логика для расчета сторон по теореме Пифагора и валидация сообщения клиента:
```Python
def LocateCalculate(data):
    if data[2] == 0:
        return (data[0] ** 2 + data[1] ** 2) ** 0.5
    elif data[1] == 0:
        return (data[2] ** 2 - data[0] ** 2) ** 0.5
    return (data[2] ** 2 - data[1] ** 2) ** 0.5

def CheckMessage(data):
    try:
        val_tuple = tuple(map(int, data.split()))
    except ValueError:
        print('Something went wrong with input')
        return False
    for i in val_tuple:
        if i < 0:
            print('Sides can not be negative')
            return False
    if (val_tuple[2] <= val_tuple[1] or val_tuple[2] <= val_tuple[0]) and val_tuple[2] != 0:
        print('Hypothenus can not be shorter than cathetus')
        return False
    return val_tuple
```
### Клиентская часть
Устанавливаем сокет клиента по TCP:
```Python
import socket

message = input()

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
```
Логика отправления и приема сообщений:
```Python
s.sendall(message.encode('utf-8'))

data = s.recv(1024)
print(data.decode('utf-8'))

data = s.recv(1024)
print(data.decode('utf-8'))

s.close()
```
### Серверная часть
Устанавливаем сокет сервера по TCP:
```Python
import socket
import sys
from func import LocateCalculate, CheckMessage

HOST = 'localhost'
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

s.listen(10)
```
Обрабатываем подключения:
```Python
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
    reply = data.decode('utf-8')
    message = 'Pythagorator 3000k\nInsert data like "leg leg hypothenus" using space as separator, mark unknown as "0", e.g. 0 3 25'
    conn.sendall(message.encode('utf-8'))
    temp = CheckMessage(reply)
    if temp:
        msg = f"The input is: {reply}\nX = {LocateCalculate(temp)}"
        conn.sendto(msg.encode('utf-8'), addr)
        print(f"sent to {addr}")

    conn.close()
```
## Задание 3
### Клиентская часть
Инициализация сокета взята из предыдущего упражнения
Отправляем запрос на сервер, получаем ответ:
```Python
request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
s.sendall(request.encode())

data = s.recv(1024)
print(data.decode('utf-8'))

s.close()
```
### Серверная часть
Инициализация сокета взята из предыдущего упражнения
Читаем файл посредством Python:
```Python
with open('index.html', 'r') as f:
    file = f.read()
```
Отправляем файл каждому подключенному пользователю:
```Python
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    conn.sendto(file.encode('utf-8'), addr)
    data = conn.recv(1024)
    conn.close()
```
## Задание 4
### Клиентская часть
Функция ожидания сообщения:
```Python
def WaitForMessage(conn):
    while True:
        try:
            data = conn.recv(1024)
            if data:
                print(data.decode('utf-8'))
        except:
            break
    conn.close()
```
Поддержка соединения у клиента:
```Python
message = 1
while message:
    th = threading.Thread(target=WaitForMessage, args=(s,))
    th.start()
    message = input()
    s.sendall(message.encode('utf-8'))

s.close()
```
### Серверная часть
Функции поддержки массовой рассылки, поддержки эмодзи и ожидания сообщения:
```Python
def Emojify(addr):
    emoji = b"\\" + f"U0001F{addr % 1000}".encode()
    return emoji.decode('unicode_escape')

def SendToAll(msg):
    for i in clients:
        i.send(msg)

def WaitForMessage(addr, conn):
    clients.append(conn)
    while True:
        try:
            data = conn.recv(1024)
            code = Emojify(addr[1])
            message = f"\n[{addr[1]}] {code} says: {data.decode('utf-8')}"
            SendToAll(message.encode('utf-8'))
        except:
            clients.remove(conn)
            SendToAll(f"{code} Disconnected".encode('utf-8'))
            break
    conn.close()
```
Непосредственно основной луп:
```Python
s.listen(10)
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    th = threading.Thread(target=WaitForMessage, args=(addr, conn))
    th.start()
```

## Задание 5
### Клиентская часть
Используется функция ожидания сообщения из прошлого задания, аналогично предыдущим заданиям инициализируется и сокет. Реализация основного лупа у клиента:
```Python
header = b'POST /subject HTTP/1.1\r\nHost: localhost\r\nAccept: text/html\r\nContent-Type: application/json\r\n' # темплейт
message = 1
while message:
    th = threading.Thread(target=WaitForMessage, args=(s,))
    th.start()
    key = input('Дисциплина: ') # ждем ввода предмета и оценки
    value = input('Оценка: ')
    son_of_j = json.dumps({key: value}) # создаем json
    request = header + f"Content-Length: {len(son_of_j)}\r\n\r\n".encode() + json.dumps({key: value}).encode('utf-8')
    s.send(request)
s.close()
```
### Серверная часть
Класс Response:
```Python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body

    def return_string(self):
        return f"{self.status} {self.reason} {self.body}"
```
Класс Request:
```Python
class Request:
    def __init__(self, method, target, version, headers, rfile, conn):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile
        self.conn = conn

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
Инициализация сервера и обслуживание клиента:
```Python
class HTTPserver():
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name

    def init_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self._host, self._port))
            self.socket.listen(10)
        except socket.error as msg:
            print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    
    def launch_server(self):
        self.init_socket()
        while True:
            conn, addr = self.socket.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))
            th = threading.Thread(target=self.serve_client, args=(conn,))
            th.start()

    def serve_client(self, conn):
        while True:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            conn.send(resp.return_string().encode())
            with open('AcademicPerformance.html') as html:
                conn.send(html.read().encode()) # sending html
        conn.close()
```
Парсеры (методы внутри класса HTTPserver):
```Python
    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        return Request(method, target, ver, headers, rfile, conn)
        
    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request', 'Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        print(req_line)
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise HTTPError(494, 'Request header too large')

            if line in (b'\r\n', b'\n', b''):
                break
            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def handle_request(self, req): # решаем кто пост, кто гет
        if req.path == '/subject' and req.method == 'POST':
            return self.handle_post(req)

        if req.path == '/subject' and req.method == 'GET':
            return self.handle_get(req)
```
Реализация работы с JSON и обновлением страницы:
```Python
    def handle_post(self, req): # успокаиваем пользователя, что мы все прочитали
        content_type = req.headers.get('Content-Type')
        accept = req.headers.get('Accept')
        if ('text/html' in accept) and ('application/json' in content_type): # проверка accept и content-type
            contentType = 'text/html; charset=utf-8'
            body = 'I can read your request'
            son_of_j = self.ExtractJson(req)
            try:
                self.CombineAndSave(son_of_j)
            except:
                return Response(500, 'Internal server error')
        else:
            return Response(406, 'Not Acceptable')
        body = body.encode('utf-8')
        headers = [('Content-Type', contentType), ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def CombineAndSave(self, d):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
            for i in d.keys(): # совмещаем json файлы
                data[i] = data.get(i, [])
                data[i].append(d[i])
        with open('data.json', mode='w', encoding='utf-8') as f: # сохраняем итоговый json
            json.dump(data, f)
        data = json2html.convert(json=data)
        with open('AcademicPerformance.html', 'w') as htmlfile: # создаем html из json
            htmlfile.write(str(data))

    def ExtractJson(self, req): # вытаскиваем контент из реквеста
        json_str = req.rfile.readline(int(req.headers.get('Content-Length')))
        return json.loads(json_str)
```
Инициализация и запуск сервера:
```Python
a = HTTPserver('localhost', 8081, 'Server')
a.launch_server()
```