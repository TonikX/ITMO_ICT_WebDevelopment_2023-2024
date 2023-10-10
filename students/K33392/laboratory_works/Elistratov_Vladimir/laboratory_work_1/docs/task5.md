##Задание 5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Задание: сделать сервер, который может:
Принять и записать информацию о дисциплине и оценке по дисциплине.
Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

##Сервер
```py
import socket
from email.parser import Parser
import sys
import socket
import re
import json

MAX_LINE = 2**16

class MyHTTPServer:
  # Параметры сервера
  def __init__(self, server_ip, server_port, num_listen=1):
    # Создаем сокет и настраиваем его параметры.
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server.bind((server_ip, server_port))  # Привязываем сокет к указанному IP и порту.
    self.server.listen(num_listen)  # Начинаем слушать входящие соединения.
    self._grades = {}  # Словарь для хранения оценок.

    # Основной цикл сервера для обслуживания клиентов.
  def serve_forever(self):
    while True:
        connection, addr = self.server.accept()  # Принимаем входящее соединение от клиента.
        self.serve_client(connection)

  def serve_client(self, connection):
    # 2. Обработка клиентского подключения
    req = self.parse_request(connection)
    resp = self.handle_request(req)
    self.send_response(connection, resp)
    pass

  def parse_request(self, connection):
    # 3. функция для обработки заголовка http+запроса. Python, сокет предоставляет возможность создать вокруг него некоторую обертку, которая предоставляет file object интерфейс. Это дайте возможность построчно обработать запрос. Заголовок всегда - первая строка. Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола). URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143 , где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
    
    rfile = connection.makefile('rb')

    method, target, ver = self.parse_request_Line(rfile)

    headers = self.parse_headers(rfile)

    return Request(method, target, ver, headers, rfile)
    
    pass

  def parse_request_Line(self, rfile):
    raw = rfile.readline()
    req_line = str(raw, 'iso-8859-1')
    words = req_line.split(' ')
    
    method, target, ver = words

    return method, target, ver

  def parse_headers(self, rfile):
    # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    headers = []
    while True:
      line = rfile.readline()
      if line in (b'\r\n', b'\n', b''):
        break
      headers.append(line)

    sheaders = b''.join(headers).decode('iso-8859-1')
    return Parser().parsestr(sheaders)

  def handle_request(self, req):
    # 5. Функция для обработки url в соответствии с нужным методом. 
    # В случае данной работы, нужно будет создать набор условий, который обрабатывает GET или POST запрос. 
    # GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
    if req.method == 'POST':
      return self.handle_post_users(req)

    if req.method == 'GET':
      return self.handle_get_users(req)

    return 0

  def send_response(self, connection, resp):
    # 6. Функция для отправки ответа. 
    # Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    #print ("IM here")
    ms = f'HTTP/1.1 {str(resp.status)} {str(resp.reason)}\r\n'
    #print ("IM here2")
    if resp.headers:
      for (key, value) in resp.headers:
        header_line = f'{str(key)}: {str(value)}\r\n'
        ms += header_line
    #print ("IM here3")
    ms += '\r\n'
    #print ("IM here4")
    if resp.body:
      print(resp.body)
      ms += str(resp.body)
    #print ("IM here5")
    connection.send(ms.encode("utf-8"))
    #print ("IM here6")
    connection.close()
    #print (ms)
    pass

  def handle_post_users(self, req):
    body = req.body()
    params = {p.split("=")[0]: p.split("=")[1] for p in body.split("&")}
    discipline = params.get("discipline")
    grade = params.get("grade")
    id = len(self._grades) + 1
    self._grades[id] = {'id': id, 'disp': discipline,'grade': grade}
    return Response(204, 'Created')
    pass

  def handle_get_users(self, req):
    accept = req.headers.get('Accept')
    contentType = 'text/html; charset=utf-8'
    body = '<html><head></head><body>'
    body += f'<div>Оценки ({len(self._grades)})</div>'
    body += '<ul>'
    for u in self._grades.values():
      body += f'<li>#{u["disp"]} {u["grade"]}</li>'
    body += '</ul>'
    body += '</body></html>'
    
    headers = [('Content-Type', contentType),
                ('Content-Length', len(body))]
    return Response(200, 'OK', headers, body)
    pass

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
  
  def body(self):
    size = (self.headers.get('Content-Length'))
    r = (self.rfile.read(int(size))).decode('utf-8')
    return r

if __name__ == '__main__':
  # host = "127.0.0.1"
  host = socket.gethostbyname(socket.gethostname()) 
  port = 14900
  print(host, ':', port)
  serv = MyHTTPServer(host, port)
  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    serv.server.close()
```

##Пример работы
![Запуск сервера](pic/t5/server.png)
![Запуск клиента](pic/t5/client.png)