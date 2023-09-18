import socket


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.students = {}  # Словарь для хранения данных о студентах и их оценках

    def serve_forever(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Client connected: {client_address[0]}:{client_address[1]}")
            self.serve_client(client_socket)

    def serve_client(self, client_socket):
        request = client_socket.recv(1024).decode()
        method, path, headers, body = self.parse_request(request)
        self.handle_request(method, path, headers, body, client_socket)

    def parse_request(self, request):
        lines = request.split("\r\n")
        if len(lines) < 1:
            raise ValueError("Invalid request: empty request")
        request_line = lines[0].split(" ")
        if len(request_line) != 3:
            raise ValueError("Invalid request: malformed request line")
        method, path, version = request_line
        if len(lines) < 2:
            raise ValueError("Invalid request: missing headers")
        headers = self.parse_headers(lines[1:])
        body = ""
        if method == "POST" and len(lines) > 2:
            body = lines[-1]
        return method, path, headers, body

    def serve_client(self, client_socket):
        request = b''
        while True:
            chunk = client_socket.recv(1024)
            request += chunk
            if len(chunk) < 1024:
                break
        if not request:
            return

        request = request.decode()
        method, path, headers, body = self.parse_request(request)
        self.handle_request(method, path, headers, body, client_socket)
        client_socket.close()



    def parse_headers(self, lines):
        headers = {}
        for line in lines:
            if line:
                parts = line.split(": ")
                if len(parts) == 2:
                    key, value = parts
                    headers[key] = value
        return headers


    def handle_request(self, method, path, headers, body, client_socket):
        if method == "GET":
            if path == "/":
                self.send_response(client_socket, 200, "OK", {"Content-Type": "text/html"}, self.generate_homepage())
            elif path == "":
                 self.send_response(client_socket, 200, "OK", {"Content-Type": "text/html"}, self.generate_homepage())
            elif path == "/add":
                self.send_response(client_socket, 200, "OK", {"Content-Type": "text/html"}, self.generate_add_page())
            else:
                self.send_response(client_socket, 404, "Not Found", {"Content-Type": "text/html"}, "<h1>404 Not Found</h1>")
        elif method == "POST":
            if path == "/add":
                self.handle_add_request(body)
                self.send_response(client_socket, 302, "Found", {"Location": "/"}, "")
            else:
                self.handle_add_request(body)
                self.send_response(client_socket, 302, "Found", {"Location": "/"}, "")
        else:
            self.send_response(client_socket, 400, "Bad Request", {"Content-Type": "text/html"}, "<h1>400 Bad Request</h1>")

    def send_response(self, client_socket, status_code, reason_phrase, headers, body=None):
        response = f"HTTP/1.1 {status_code} {reason_phrase}\r\n"
        for key, value in headers.items():
            response += f"{key}: {value}\r\n"
        response += "\r\n"
        if body:
            response += body
        client_socket.sendall(response.encode())
        client_socket.close()

    def generate_homepage(self):
        html = "<h1>Grades</h1>"
        html += "<table>"
        html += "<tr><th>Discipline</th><th>Grade</th></tr>"
        for discipline, grade in self.students.items():
            html += f"<tr><td>{discipline}</td><td>{grade}</td></tr>"
        html += "</table>"
        html += "<a href='/add'>Add Grade</a>"
        return html

    def generate_add_page(self):
        html = "<h1>Add Grade</h1>"
        html += "<form method='POST' action='/add'>"
        html += "<label for='discipline'>Discipline:</label>"
        html += "<input type='text' id='discipline' name='discipline'><br>"
        html += "<label for='grade'>Grade:</label>"
        html += "<input type='number' id='grade' name='grade' min='1' max='5'><br>"
        html += "<input type='submit' value='Add Grade'>"
        html += "</form>"
        html += "<a href='/'>Back to Homepage</a>"
        return html

    def handle_add_request(self, body):
        params = self.parse_params(body)
        discipline = params.get("discipline")
        grade = params.get("grade")
        if discipline and grade:
            if grade.isdigit() and 1 <= int(grade) <= 5:
                self.students[discipline] = int(grade)


    def parse_params(self, body):
        params = {}
        if body:
            pairs = body.split("&")
            for pair in pairs:
                key, value = pair.split("=")
                params[key] = value
        return params

if __name__ == '__main__':
    host = 'localhost'  # Адрес сервера
    port = 8080  # Порт сервера
    name = 'MyHTTPServer/1.0'  # Имя сервера
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
