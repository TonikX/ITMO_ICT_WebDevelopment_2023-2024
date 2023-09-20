import http.server
import urllib.parse

# Запись оценок
grades = {}

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # HTML-форма для добавления оценки
            html = """
                <html>
                <head><title>Add Grade</title></head>
                <body>
                <h1>Add Grade</h1>
                <form method="POST" action="/add_grade">
                    <label for="subject">Subject:</label><br>
                    <input type="text" id="subject" name="subject"><br>
                    <label for="grade">Grade:</label><br>
                    <input type="number" id="grade" name="grade" min="1" max="5"><br><br>
                    <input type="submit" value="Submit">
                </form>
                <p><a href="/grades">Grades Overview</a></p>
                </body></html>
            """
            self.wfile.write(bytes(html, "utf8"))
            return
        elif self.path == '/grades':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Страница с обзором оценок в виде таблицы
            html = """
                <html>
                <head><title>Grades Overview</title></head>
                <body>
                <h1>Grades Overview</h1>
                <table border="1">
                <tr>
                    <th>Subject</th>
                    <th>Grade</th>
                </tr>
            """
            for subject, grade in grades.items():
                html += f"<tr><td>{subject}</td><td>{grade}</td></tr>"
            html += "</table>"
            html += "<p><a href='/'>Add Grade</a></p>"
            html += "</body></html>"
            self.wfile.write(bytes(html, "utf8"))
            return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        subject = params['subject'][0]
        grade = params['grade'][0]
        try:
            grade = int(grade)
            if grade < 1 or grade > 5:
                raise ValueError("Grade out of range")
            grades[subject] = grade
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        except ValueError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(bytes("Bad request. Grade must be between 1 and 5.", "utf8"))

# Создание объекта обработчика запросов
handler_object = MyHttpRequestHandler
# Создание HTTP-сервера
my_server = http.server.HTTPServer(("localhost", 8080), handler_object)
print("Server is running on localhost:8080...")
# Запуск сервера
my_server.serve_forever()
