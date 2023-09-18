# HTTP - Server side

import socket
import sys


MAX_LINE = 64*1024
MAX_HEADERS = 100


class Request:
    def __init__(self, method, url, version, headers, rfile):
        self.method = method
        self.url = url
        self.version = version
        self.headers = headers
        self.rfile = rfile
        self.body = self.set_body()

    def set_body(self):
        try:
            size = int(self.headers.get('Content-Length'))
        except:
            return
        body = self.rfile.read(size)
        return str(body, 'iso-8859-1').strip()

    @property
    def path(self):
        return self.url.split('?')[0] if '?' in self.url else self.url

    @property
    def query(self):
        if self.method == 'GET':
            query_string = self.url.split('?')[1] if '?' in self.url else None
        else:
            query_string = self.body
        if not query_string:
            return
        query_list = query_string.split('&') if '&' in query_string else [query_string]
        query_pairs = [tuple(x.split('=')) for x in query_list]
        return {key: val for key, val in query_pairs}


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._subjects = {}

    # 1. Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        print("Server running...")
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()
            while True:
                conn, addr = serv_sock.accept()
                print(f"Connected to a client at {addr}")
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed.\nDetails:', e)
        finally:
            serv_sock.close()

    # 2. Обработка клиентского подключения
    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            status = 500
            reason = b'Internal Server Error'
            body = str(e).encode('utf-8')
            resp = Response(status, reason,
                            [('Content-Length', len(body))],
                            body)
            self.send_response(conn, resp)

        if conn:
            conn.close()

    # 3. функция для обработки заголовка http+запроса.
    # Python, сокет предоставляет возможность создать вокруг него некоторую обертку,
    # которая предоставляет file object интерфейс. Это дайте возможность построчно обработать запрос.
    # Заголовок всегда - первая строка.
    # Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола).
    # URL необходимо разбить на адрес и параметры
    # (isu.ifmo.ru/pls/apex/f?p=2143 , где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
    def parse_request(self, conn):
        rfile = conn.makefile('rb')

        raw = rfile.readline(MAX_LINE + 1)  # cчитываем первую строку (status line)
        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')
        req_line = str(raw, 'iso-8859-1').rstrip('\r\n')

        words = req_line.split()
        if len(words) != 3:  # должно быть 3 части через пробел
            raise Exception('Incorrect request line')
        method, url, version = words
        print('Received request: ', *words)
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')

        return Request(method, url, version, headers, rfile)


    # 4. Функция для обработки headers.
    # Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''): # секция заголовков заканчивается пустой строкой
                break

            headers.append(line.strip())
            if len(headers) > MAX_HEADERS:
                raise Exception('Too many headers')
        decoded_headers = [tuple(header.decode('iso-8859-1').split(': ')) for header in headers]
        headers_dict = dict(decoded_headers)
        print('With headers: ', headers_dict)
        return headers_dict


    # 5. Функция для обработки url в соответствии с нужным методом.
    # В случае данной работы, нужно будет создать набор условий, который обрабатывает GET или POST запрос.
    # GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
    def handle_request(self, req):
        if req.path == '/':
            contentType = 'text/html; charset=utf-8'
            with open("index.html") as index:
                body = index.read()
            body = body.encode('utf-8')
            print('Formed GET-response with body: ', body)
            headers = [('Content-Type', contentType),
                       ('Content-Length', len(body))]
            return Response(200, 'OK', headers, body)

        if req.path == '/grades' and req.method == 'POST':
            subject = req.query['subject']
            grade = req.query['grade']
            print(subject, grade)
            if subject in self._subjects:
                self._subjects[subject].append(grade)
            else:
                self._subjects[subject] = [grade]
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<h3>Grade {grade} for subject {subject} is registered.</h3>'
            body += '<br><a href="/">Return to main page</a>'
            body += '</body></html>'
            body = body.encode('utf-8')
            print('Formed POST-response with body: ', body)
            headers = [('Content-Type', contentType),
                       ('Content-Length', len(body))]
            return Response(200, 'Grade added', headers, body)

        if req.path == '/grades' and req.method == 'GET':
            subject = req.query['subject']
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<h3>Grades for subject {subject}</h3>'
            body += '<ul>'
            if subject in self._subjects.keys():
                for grade in self._subjects[subject]:
                    body += f'<li>{grade}</li>'
            else:
                body += f'<li>No grades yet</li>'
            body += '</ul>'
            body += '<br><a href="/">Return to main page</a>'
            body += '</body></html>'
            body = body.encode('utf-8')
            print('Formed GET-response with body: ', body)
            headers = [('Content-Type', contentType),
                       ('Content-Length', len(body))]
            return Response(200, 'OK', headers, body)

        raise Exception('Not found')


    # 6. Функция для отправки ответа.
    # Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    def send_response(self, conn, resp):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
            for key, value in resp.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()
        print('Response sent\n')


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

