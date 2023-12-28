import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import urlparse
from urllib.parse import parse_qs

MAX_LINE = 64*1024

"""
# добавить оценку по дисциплине
POST /journal/add?subject=Maths&mark=4

# Получение списка оценок по дисциплинам
GET /journal

"""


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



if __name__ == '__main__':
    host = 'localhost'
    port = 5321
    name = "name"

    serv = MyHTTPServer(host=host, port=port, name=name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
