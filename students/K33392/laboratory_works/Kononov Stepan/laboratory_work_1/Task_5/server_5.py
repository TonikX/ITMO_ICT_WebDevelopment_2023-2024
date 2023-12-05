import socket
from urllib.parse import parse_qs


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.data = {}

    def serve_forever(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Server is listening on {self.host}:{self.port}")

        try:
            while True:
                client_socket, client_address = server_socket.accept()
                self.serve_client(client_socket)
        except KeyboardInterrupt:
            server_socket.close()
            print("Server shutdown")

    def serve_client(self, client_socket):
        request_data = client_socket.recv(1024).decode('utf-8')
        method, url, _ = self.parse_request(request_data)
        body = request_data.split('\r\n')[-1]

        if method == 'GET':
            if url == '/grades':
                response = self.get_grades()
            else:
                response = "HTTP/1.1 404 Not Found\n\nPage not found"
        elif method == 'POST':
            if url == '/add_grade':
                response = self.add_grade(body)
            else:
                response = "HTTP/1.1 404 Not Found\n\nPage not found"
        else:
            response = "HTTP/1.1 405 Method Not Allowed\n\nMethod not allowed"

        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

    def parse_request(self, request_data):
        lines = request_data.split('\n')
        method, url, _ = lines[0].split()
        return method, url, _

    def handle_request(self, method, url, headers):
        if method == 'GET':
            if url == '/grades':
                return self.get_grades()
            else:
                return "HTTP/1.1 404 Not Found\n\nPage not found"
        elif method == 'POST':
            if url == '/add_grade':
                return self.add_grade(headers)
            else:
                return "HTTP/1.1 404 Not Found\n\nPage not found"
        else:
            return "HTTP/1.1 405 Method Not Allowed\n\nMethod not allowed"

    def add_grade(self, body):
        discipline, grade = self.parse_body_add_grade(body)

        if discipline and grade:
            self.data[discipline] = grade
            return "HTTP/1.1 200 OK\n\nGrade added successfully"
        else:
            return "HTTP/1.1 400 Bad Request\n\nInvalid request parameters"

    def parse_body_add_grade(self, body):
        parsed_body = parse_qs(body)

        discipline = parsed_body.get('Discipline', [None])[0]
        grade = parsed_body.get('Grade', [None])[0]

        return discipline, grade

    def get_grades(self):
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        response += "<html><body><h1>Grades</h1>"
        for discipline, grade in self.data.items():
            response += f"<p>{discipline}: {grade}</p>"
        response += "</body></html>"
        return response


if __name__ == '__main__':
    host = "localhost"
    port = 8080
    name = "MyHTTPServer"
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
