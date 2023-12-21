from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    # Словарь для хранения информации о дисциплине и оценках
    data = {}

    def do_POST(self):
        # Получение данных из POST-запроса
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Разделение данных на дисциплину и оценку
        discipline, grade = post_data.split('&')
        discipline = discipline.split('=')[1]
        grade = grade.split('=')[1]

        # Запись данных в словарь
        if discipline not in self.data:
            self.data[discipline] = []
        self.data[discipline].append(grade)

        # Отправка успешного ответа
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Данные записаны')

    def do_GET(self):
        # Создание HTML-страницы с информацией об оценках по дисциплине

        html = '<html><body>'
        for discipline, grades in self.data.items():
            html += '<h3>' + discipline + '</h3>'
            html += '<ul>'
            for grade in grades:
                html += '<li>' + grade + '</li>'
            html += '</ul>'
        html += '</body></html>'

        # Отправка HTML-страницы
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MyServer, port=6332):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Сервер работает на порте', port)
    httpd.serve_forever()


run()
