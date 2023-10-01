import socket
import sys


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.marks = {}

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()

        while True:
            client_socket, client_address = server.accept()
            self.serve_client(client_socket)

    def serve_client(self, client_socket):
        data, http_method, params_dict = self.parse_request(client_socket)
        headers = self.parse_headers(data)
        resp = self.handle_request(http_method, params_dict)
        self.send_response(client_socket, resp)

    def parse_request(self, client_socket):
        data = client_socket.recv(16384).decode("UTF-8").split('\n')
        http_method, http_url, http_version = data[0].split()
        params_dict = {}
        params = http_url.split("?")[1].split("&")
        for param in params:
            name, value = param.split('=')
            params_dict[name] = value
        return data, http_method, params_dict

    def parse_headers(self, data):
        headers = []
        for line in data:
            if line == '':
                break
            headers.append(line)
        return headers

    def handle_request(self, http_method, params_dict):
        if http_method == 'POST':
            name = params_dict['name']
            value = params_dict['value']
            if name in self.marks:
                self.marks[name].append(value)
            else:
                self.marks[name] = [value]
            return Response(200, 'OK')
        elif http_method == 'GET':
            name = params_dict['name']
            if name in self.marks:
                marks = self.marks[name]
                return Response(200, f"<b>{marks}</b>")
            else:
                return Response(404, 'Not found.')

    def send_response(self, client_socket, resp):
        wfile = client_socket.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('utf-8'))
        wfile.flush()
        wfile.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 14900
    server = MyHTTPServer(host, port)
    server.serve_forever()
