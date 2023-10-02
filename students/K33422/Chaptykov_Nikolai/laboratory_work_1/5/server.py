import socket
import sys
import threading
import json
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse
from json2html import *

def SendToAll(msg):
    pass

MAX_LINE = 64*1024
MAX_HEADERS = 100


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body

    def return_string(self):
        return f"{self.status} {self.reason} {self.body}"


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

    def handle_get(self, req):
        accept = req.headers.get('Accept')
        contentType = 'application/json; charset=utf-8'
        with open('data.json', mode='r', encoding='utf-8') as f: # открваем json
            body = json.load(f)
        body = body.encode('utf-8')
        headers = [('Content-Type', contentType), ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

a = HTTPserver('localhost', 8081, 'Server')
a.launch_server()
