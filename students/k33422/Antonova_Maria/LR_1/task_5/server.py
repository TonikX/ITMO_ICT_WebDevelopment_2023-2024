import http.server
import socketserver
import urllib.parse

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open('data.txt', 'r', encoding='utf-8') as f:
                data = f.read()
                html = '''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Оценки</title>
                </head>
                <body>
                    <h2>Оценки</h2>
                    <ul>
                        {}
                    </ul>
                    <a href="/form" style="color: black;">+ Добавить дисциплину</a>
                </body>
                </html>
                '''.format(data)
                self.wfile.write(bytes(html, 'utf8'))
            print("GET request processed, data sent to client.")
        elif self.path == '/form':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open('form.html', 'r', encoding='utf-8') as f:
                form_data = f.read()
                self.wfile.write(bytes(form_data, 'utf8'))
            print("GET request for form.html processed, form sent.")
        else:
            self.send_response(404)
            print("GET request for unknown resource, 404 sent.")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        subject = post_data.get('subject', [''])[0]
        grade = post_data.get('grade', [''])[0]
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write('<li>' + subject + ' - ' + grade + '</li>\n')
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()
        print("POST request processed, data saved.")

handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

print("Server started at http://localhost:" + str(PORT))
my_server.serve_forever()

