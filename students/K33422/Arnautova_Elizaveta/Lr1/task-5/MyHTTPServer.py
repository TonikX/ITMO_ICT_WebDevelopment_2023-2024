import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse
from template import HTML_STYLE, ADD_GRADE, NO_PAGE, YOUR_MARKS, STARTER, ADDER

HOST = '127.0.0.1'
SERVER_PORT = 14901

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class Request:  # обрабатывает HTTP-запросы и предоставляет свойства для доступа к различным частям запроса.
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
    def body(self):
        size = self.headers.get('Content-Length')
        if not size:
            return None
        content = self.rfile.read(int(size))
        return content.decode('utf-8')

    @property
    @lru_cache(maxsize=None)
    def url(self):
        return urlparse(self.target)

    @property
    @lru_cache(maxsize=None)
    def query(self):
        return parse_qs(self.url.query)

    @property
    @lru_cache(maxsize=None)
    def query_body(self):
        return parse_qs(self.body)


class Response:  # представляет HTTP-ответ и его состояние
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    def __init__(self, server_address):
        self.server_address = server_address
        self.conn = None
        self.grades = {}

    def serve_forever(self):  # начинает прослушивание входящих запросов и обрабатывает их
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_sock.bind(self.server_address)
            server_sock.listen(10)
            print("Server is listening...")
            while True:
                client_socket, _ = server_sock.accept()
                try:
                    self.serve_client(client_socket)
                except Exception as e:
                    print('Connection failed', e)
        finally:
            server_sock.close()
            print("Server stopped")

    def serve_client(self, conn):  # обрабатывает входящий запрос от клиента
        try:
            req = self.parse_request(conn)
            response = self.handle_request(req)
            self.send_response(conn, response)  # отправляет ответ
        except ConnectionResetError:
            conn = None
        except Exception as e:
            print("Error", e)
        if conn:
            conn.close()

    def parse_request(self, conn):  # анализирует запрос, полученный от клиента
        rfile = conn.makefile('rb')
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()
        if len(words) != 3:
            raise Exception('Malformed request line')

        method, target, version = words
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        headers = self.parse_headers(rfile)

        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')

        return Request(method, target, version, headers, rfile)

    @staticmethod
    def parse_headers(rfile):  # анализирует заголовки запроса
        headers = []

        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''):  # прерывается, когда находится пустая строка
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise Exception('Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def handle_request(self, req):  # обрабатывает проанализированный запрос и возвращает соответствующий ответ
        if req.path == '/' and req.method == 'POST':  # проверяет путь и метод запроса, чтобы определить действие,
            return self.handle_post(req)  # которое необходимо предпринять.
        if req.method == 'GET':
            if req.path == '/add_grade':
                body = STARTER + HTML_STYLE + ADD_GRADE
                return self.handle_get(body)

            elif req.path == '/':
                return self.handle_get()

        content = STARTER + HTML_STYLE + NO_PAGE
        return self.handle_get(content)

    def handle_get(self, body=None):  # обрабатывает запросы GET и подготавливает тело ответа
        content_type = 'text/html; charset=utf-8'
        if body is None:
            body = STARTER + HTML_STYLE + YOUR_MARKS
            for subject, grades in self.grades.items():  # добавляет информацию о предмете и оценках в тело ответа
                grade = []
                for g in grades:
                    grade.append(g)
                body += f"""
                        <tr>
                            <td style="border: 1px solid black; padding: 4px;">{subject}</td>
                            <td style="border: 1px solid black; padding: 4px;">{', '.join(grade)}</td>
                        </tr>
                    """

            body += ADDER

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, req):  # обрабатывает запросы POST и обновляет словарь self.grades
        subject = req.query_body['subject'][0]
        grade = req.query_body['grade'][0]
        try:  # добавляет оценку в существующий список
            self.grades[subject].append(grade)
        except KeyError:  # создает новую пару ключ-значение в словаре self.grades.
            self.grades[subject] = [grade]
        return self.handle_get()  # вызывает метод handle_get для генерации ответа с обновленными оценками.

    @staticmethod
    def send_response(conn, resp):  # отправляет HTTP-ответ клиенту
        wfile = conn.makefile('wb')
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


if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    my_server = MyHTTPServer(server_address)
    my_server.serve_forever()
