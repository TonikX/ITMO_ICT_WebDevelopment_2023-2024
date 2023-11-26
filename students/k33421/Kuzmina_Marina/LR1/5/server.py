import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse
MAX_LINE = 64 * 1024
MAX_HEADERS = 100

class MyHTTPServer:

    def __init__(self, method, target, version, headers, rfile):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile

    @property
    def path(self):
        return self.parsed_url.path

    @property
    def body(self):
        size = self.headers.get('Content-Length')
        if not size:
            return None
        content = self.rfile.read(int(size))
        return content.decode('utf-8')

    @property
    @lru_cache(maxsize=None)
    def parsed_url(self):
        return urlparse(self.target)

    @property
    @lru_cache(maxsize=None)
    def query_parameters(self):
        return parse_qs(self.parsed_url.query)

    @property
    @lru_cache(maxsize=None)
    def form_parameters(self):
        return parse_qs(self.body)


class CustomResponse:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class HTTPServer:
    def __init__(self, server_address):
        self.server_address = server_address
        self.connection = None
        self.grades_data = {}  # {subject: [grades]}

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind(self.server_address)
            server_socket.listen(10)
            print("Server is running...")
            while True:
                client_socket, _ = server_socket.accept()
                try:
                    self.handle_client(client_socket)
                except Exception as e:
                    print('Connection failed', e)
        finally:
            server_socket.close()
            print("Server stopped")

    def handle_client(self, conn):
        try:
            request = self.parse_request(conn)
            response = self.handle_request(request)
            self.send_response(conn, response)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            print("Error", e)
        if conn:
            conn.close()

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        raw_request = rfile.readline(MAX_LINE + 1)
        if len(raw_request) > MAX_LINE:
            raise Exception('Request line is too long')

        request_line = str(raw_request, 'iso-8859-1')
        request_line = request_line.rstrip('\r\n')
        method, target, version = request_line.split()
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')

        return MyHTTPServer(method, target, version, headers, rfile)

    @staticmethod
    def parse_headers(rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise Exception('Too many headers')

        parsed_headers = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(parsed_headers)

    def handle_request(self, request):
        if request.path == '/' and request.method == 'POST':
            return self.handle_post(request)
        if request.method == 'GET':
            if request.path == '/add_grade':
                body = """<!DOCTYPE html>
                        <html lang="ru">
                        <style>
                            body {
                                font-family: Montserrat, sans-serif;
                                background-color: #e3ecfa;
                                text-align: center;
                                padding: 200px;
                            }
                            h2 {
                                color: #8ab2f2;
                            }
                            p {
                                color: #666;
                                font-size: 20px;
                            }
                        </style>
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        </head>
                        <script>
                            // JavaScript скрипты здесь
                        </script>
                        <body>
                            <h2>ENTER THE GRADE</h2>
                            <form method="POST" action="/">
                                <input type="text" id="subject" name="subject" placeholder="Subject">
                                <input type="text" id="grade" name="grade" placeholder="Grade">
                                <input type="submit" value="Send" style="background-color: #8ab2f2; color: #fff; padding: 10px 20px; border: none; cursor: pointer;border-radius: 20px;">
                            </form>
                            <form action="/">
                                <input type="submit" value="To the main page"/ style="background-color: #8ab2f2; color: #fff; padding: 10px 20px; border: none; cursor: pointer;border-radius: 20px;">
                            </form>
                        </body>
                        """
                return self.handle_get(body)
            elif request.path == '/':
                return self.handle_get()
        content = """<!DOCTYPE html>
                <html lang="ru">
                <style>
                    body {
                        font-family: Montserrat, sans-serif;
                        background-color: #e3ecfa;
                        text-align: center;
                        padding: 200px;
                    }
                    h2 {
                        color: #8ab2f2;
                    }
                    p {
                        color: #666;
                        font-size: 20px;
                    }
                </style>
                <body>
                    <h2>Error 404</h2>
                    <form action="/">
                        <input type="submit" value="To the main page"/ style="background-color: #8ab2f2; color: #fff; padding: 10px 20px; border: none; cursor: pointer;border-radius: 20px;">
                    </form>
                </body>
                </html>
                """
        return self.handle_get(content)

    def handle_get(self, body=None):
        content_type = 'text/html; charset=utf-8'
        if body is None:
            body = """
                <!DOCTYPE html>
                <html lang="ru">
                <style>
                    body {
                        font-family: Montserrat, sans-serif;
                        background-color: #e3ecfa;
                        text-align: center;
                        padding: 200px;
                    }
                    h2 {
                        color: #8ab2f2;
                    }
                    p {
                        color: #8ab2f2;
                        font-size: 20px;
                    }
                </style>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                </head>
                <body>
                    <h2>YOUR GRADES</h2>
                    <table>
                        <tr>
                            <th>Subject</th>
                            <th>Grade</th>
                        </tr>
                """
            for subject, grades in self.grades_data.items():
                for grade in grades:
                    body += f"""
                            <tr>
                                <td>{subject}</td>
                                <td>{grade}</td>
                            </tr>
                        """

            body += """
                    </table>
                    <form action="/add_grade">
                        <input type="submit" value="Add grade" style="background-color: #8ab2f2; color: #fff; padding: 10px 20px; border: none; cursor: pointer;border-radius: 20px;">
                    </form>
                </body>
                </html>
                """

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return CustomResponse(200, 'OK', headers, body)

    def handle_post(self, request):
        subject = request.form_parameters['subject'][0]
        grade = request.form_parameters['grade'][0]
        try:
            self.grades_data.setdefault(subject, []).append(grade)
        except KeyError:
            self.grades_data[subject] = [grade]
        return self.handle_get()

    @staticmethod
    def send_response(conn, response):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {response.status} {response.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if response.headers:
            for (key, value) in response.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if response.body:
            wfile.write(response.body)

        wfile.flush()
        wfile.close()


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8080)
    http_server = HTTPServer(server_address)
    http_server.start()
