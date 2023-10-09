import socket
import sys
import urllib.parse

class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.grades = {}
        self.server_socket = None
        self.client_socket = None
        self.running = False

    def serve_forever(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is running on http://{self.host}:{self.port}")
        self.running = True

        while self.running:
            try:
                self.client_socket, client_address = self.server_socket.accept()
                self.serve_client()
            except KeyboardInterrupt:
                self.exit()

    def serve_client(self):
        request_data = self.client_socket.recv(1024).decode('utf-8')
        method, path = self.parse_request(request_data)
        headers = self.parse_headers(request_data)

        if method == "GET":
            response = self.handle_get_request(path)
        elif method == "POST":
            data_length = int(headers.get("Content-Length", 0))
            response = self.handle_post_request(path, request_data[-data_length:])
        else:
            response = "HTTP/1.1 405 Method Not Allowed\r\n\r\nMethod not supported"

        self.client_socket.sendall(response.encode('utf-8'))
        self.client_socket.close()

    def parse_request(self, request_data):
        lines = request_data.strip().split("\r\n")
        method, full_path, _ = lines[0].split(' ')
        parsed_url = urllib.parse.urlparse(full_path)
        path = parsed_url.path
        return method, path

    def parse_headers(self, request_data):
        lines = request_data.strip().split("\r\n")
        headers = {}
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key] = value
        return headers

    def handle_get_request(self, path):
        if path == "/":
            form = """
               <form method="POST" action="/add_grade">
                   <label for="subject">Subject:</label>
                   <input type="text" id="subject" name="subject" required><br>
                   <label for="grade">Grade:</label>
                   <input type="text" id="grade" name="grade" required><br>
                   <input type="submit" value="Add Grade">
               </form>
            """
            grade_table = self.generate_grade_table()
            page = f"List of disciplines and grades:<br>{grade_table}<br>{form}"
            response = f"HTTP/1.1 200 OK\r\nServer: {self.name}\r\nContent-Type: text/html\r\n\r\n{page}"
        else:
            response = f"HTTP/1.1 404 Not Found\r\nServer: {self.name}\r\n\r\nPage not found"
        return response


    def handle_post_request(self, path, request_body):
        if path == "/add_grade":
            query_params = urllib.parse.parse_qs(request_body)
            subject = query_params.get("subject", [''])[0]
            grade = query_params.get("grade", [""])[0]
            if subject in self.grades:
                self.grades[subject].append(grade)
            else:
                self.grades[subject] = [grade]
            page = """
                <h1>Successufully added!</h1>
                <button onclick="window.location.href = '/'">Back to home</button>
            """
            response = f"HTTP/1.1 201 Created\r\nServer: {self.name}\r\nContent-Type: text/html\r\n\r\n{page}"
        else:
            response = f"HTTP/1.1 404 Not Found\r\nServer: {self.name}\r\n\r\nPage not found"
        return response

    def generate_grade_table(self):
        table = "<table border='1'><tr><th>Subject</th><th>Grade</th></tr>"
        for subject, grades in self.grades.items():
            string = ''
            for i in range(len(grades) - 1):
                string += str(grades[i]) + ', '
            string += str(grades[(len(grades) - 1)])
            table += f"<tr><td>{subject}</td><td>{string}</td></tr>"
        table += "</table>"
        return table

    def exit(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        if self.client_socket:
            self.client_socket.close()
        print("Server closed")


if __name__ == '__main__':
    host = "localhost"
    port = 12394
    name = "MyServer"
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        serv.exit()
        sys.exit(0)
