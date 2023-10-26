import socket
from discipline_controller import DisciplineController
import json
import sys


class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server_socket = None

        self.method = None
        self.url = None
        self.protocol = None
        self.parameters = {}
        self.post_data = {}
        self.headers = {}

        self.discipline_controller = DisciplineController()

    def serve_forever(self):
        server_socket = socket.socket()
        server_socket.bind((self.host, self.port))
        server_socket.listen()

        self.server_socket = server_socket

        while True:
            self.serve_client()

    def serve_client(self):
        client_socket, addr = self.server_socket.accept()
        request = client_socket.recv(1024)
        try:
            self.parse_request(request)
            response = self.handle_request()
            self.send_response(client_socket, response)
            print('response sent successfully')
        except ValueError as e:
            print('empty request')
        except Exception as e:
            print(e)

    def parse_request(self, request):
        request = request.decode('utf-8')
        request = request.split('\r\n')

        method, url, protocol = request[0].split(' ')
        self.method, self.url, self.protocol = method.strip(' '), url.strip(' '), protocol.strip(' ')

        # GET parameters
        parameters = {}

        if len(url.split('?')) > 1:
            url, raw_parameters = url.split('?')

            self.url = url

            raw_parameters = raw_parameters.split('&')
            for parameter in raw_parameters:
                name, value = parameter.split('=')
                parameters[name] = value

        self.parameters = parameters

        headers_stop_index = request.index('')
        self.headers = self.parse_headers(request[1:headers_stop_index])

        # POST parameters
        if method == 'POST':
            raw_data = ''.join(request[headers_stop_index + 1:])
            self.post_data = json.loads(raw_data)

    def parse_headers(self, headers):
        parsed_headers = {}

        for header in headers:
            name, value = header.split(':', 1)
            name, value = name.strip(' '), value.strip(' ')
            parsed_headers[name] = value

        return parsed_headers

    def handle_request(self):
        try:
            route = self.get_routes()[self.url][self.method]
            if self.method == 'GET':
                return getattr(route['controller'], route['method'])(self.parameters)
            elif self.method == 'POST':
                return getattr(route['controller'], route['method'])(self.post_data)
        except KeyError as e:
            with open('C:\\Users\\tyumi\\Desktop\\web\\students\\k33402\\Tiumin_Nikita\\l1\\5_web_server\\not_found.html', 'r') as f:
                html = f.read()
            return {'type': 'html', 'code': 404, 'data': html}

    def send_response(self, client_socket, response):
        reasons = {
            200: 'OK',
            404: 'NOT FOUND',
            422: 'UNPROCESSABLE ENTITY',
        }

        if response["type"] == 'html':
            response_body_raw = response["data"].encode('utf-8')
        else:
            response_body_raw = json.dumps(response['data']).encode('utf-8')

        response_headers = {
            'Content-Type': f'{"text/html" if response["type"] == "html" else "application/json"}; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        client_socket.send(f'{self.protocol} {response["code"]} {reasons[response["code"]]}\n'.encode('utf-8'))  # status line
        client_socket.send(''.join(f'{name}: {response_headers[name]}\n' for i, name in enumerate(response_headers)).encode('utf-8'))  # headers
        client_socket.send('\n'.encode('utf-8'))
        client_socket.send(response_body_raw)  # body

    def get_routes(self):
        return {
            '/disciplines': {
                'GET': {'controller': self.discipline_controller, 'method': 'index'},
                'POST': {'controller': self.discipline_controller, 'method': 'store'},
            }
        }


if __name__ == '__main__':
    host = ''
    port = 9000
    name = 'name'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
