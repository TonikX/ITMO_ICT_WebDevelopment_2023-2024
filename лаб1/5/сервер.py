import socket

class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def serve_forever(self):
        print(f"Listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                self.serve_client(client_socket)
        except KeyboardInterrupt:
            print("Server terminated.")
            self.server_socket.close()

    def serve_client(self, client_socket):
        request_data = client_socket.recv(1024).decode("utf-8")
        if not request_data:
            client_socket.close()
            return

        method, url, _ = self.parse_request(request_data)
        headers = self.parse_headers(request_data)
        response_data = self.handle_request(method, url, headers, client_socket)
        self.send_response(client_socket, response_data)
        client_socket.close()

    def parse_request(self, request_data):
        lines = request_data.split("\r\n")
        request_line = lines[0].split()
        method, url, protocol = request_line
        url_parts = url.split("?")
        path = url_parts[0]
        params = {}
        if len(url_parts) > 1:
            params = dict(param.split("=") for param in url_parts[1].split("&"))
        return method, path, params

    def parse_headers(self, request_data):
        headers = {}
        lines = request_data.split("\r\n")[1:]
        for line in lines:
            if not line:
                break
            key, value = line.split(": ", 1)
            headers[key] = value
        return headers

    def handle_request(self, method, path, headers, client_socket):
        if method == "GET":
            if path == "/":
                return self.get_home_page()
            elif path == "/grades":
                return self.get_grades_page()
        elif method == "POST":
            if path == "/add_grade":
                content_length = int(headers.get("Content-Length", 0))
                data = self.receive_data(content_length, client_socket)
                return self.add_grade(data)
        return self.not_found()

    def receive_data(self, content_length, client_socket):
        data = b""
        while content_length > 0:
            chunk = client_socket.recv(1024)

            if not chunk:
                break
            data += chunk
            content_length -= len(chunk)
        return data.decode("utf-8")

    def send_response(self, client_socket, response_data):
        client_socket.sendall(response_data.encode("utf-8"))

    def get_home_page(self):
        return """HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body><h2>Введите информацию о дисциплине и оценке:</h2><form method='POST' action='/add_grade'><label for='discipline'>Дисциплина:</label><input type='text' name='discipline' required><br><label for='grade'>Оценка:</label><input type='text' name='grade' required><br><input type='submit' value='Отправить'></form></body></html>"""

    def get_grades_page(self):
        return """HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body><h2>Оценки по дисциплине:</h2><ul><li>Математика: 4.5</li><li>Физика: 5.0</li></ul></body></html>"""

    def add_grade(self, data):
        return """HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body><h2>Оценка успешно добавлена!</h2></body></html>"""

    def not_found(self):
        return """HTTP/1.1 404 Not Found\r\n\r\nPage Not Found"""

if __name__ == '__main__':
    host = 'localhost'
    port = 8080
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
