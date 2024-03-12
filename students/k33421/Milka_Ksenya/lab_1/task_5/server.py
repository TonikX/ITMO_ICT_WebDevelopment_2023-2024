import socket
import threading
from http.client import responses
from urllib.parse import parse_qs, unquote_plus

from config import BUFF_SIZE, HOST, PORT


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.records = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.lock = threading.Lock()

    def run(self):
        print(f"Server running at http://{self.host}:{self.port}")
        print("GET POST /records")

        while True:
            conn, _ = self.server_socket.accept()
            threading.Thread(target=self.manage_connection, args=(conn,)).start()

    def manage_connection(self, conn):
        response = None
        try:
            request = self.get_request(conn)
            response = self.route_request(request)
        except Exception as e:
            response = self.create_http_response(500, f"Server Error: {str(e)}")
        finally:
            conn.sendall(response)
            conn.close()

    def get_request(self, conn):
        request_data = ""

        while True:
            data = conn.recv(BUFF_SIZE).decode()
            request_data += data
            if '\r\n\r\n' in data:
                break

        return request_data

    def route_request(self, request):
        try:
            headers, body = request.split('\r\n\r\n', 1)
            method, path, _ = headers.splitlines()[0].split()
            if method == 'GET':
                return self.process_get_request(path)
            elif method == 'POST':
                return self.process_post_request(path, body)
            else:
                return self.create_http_response(405, "Method Not Allowed")
        except Exception as e:
            return self.create_http_response(400, f"Bad Request: {str(e)}")

    def process_get_request(self, path):
        if path == '/records':
            html_content = self.generate_html_records()
            return self.create_http_response(200, html_content, 'text/html')
        else:
            return self.create_http_response(404, "Page Not Found")

    def process_post_request(self, path, body):
        if path == '/records':
            data = self.parse_form_data(body)
            subject = data.get('subject')
            mark = data.get('mark')
            if subject and mark:
                self.add_record(subject, mark)
                return self.process_get_request('/records')
            else:
                return self.create_http_response(400, "Invalid Data Provided")
        else:
            return self.create_http_response(404, "Page Not Found")

    def add_record(self, subject, mark):
        with self.lock:
            self.records.setdefault(subject, []).append(mark)

    @staticmethod
    def create_http_response(status_code, content, content_type='text/plain'):
        response_headers = {
            'Content-Type': content_type,
            'Content-Length': str(len(content.encode()))
        }
        response_header = "\r\n".join([f"{k}: {v}" for k, v in response_headers.items()])
        return f"HTTP/1.1 {status_code} {responses[status_code]}\r\n{response_header}\r\n\r\n{content}".encode()

    @staticmethod
    def parse_form_data(body):
        return {k: unquote_plus(v[0]) for k, v in parse_qs(body).items()}

    def generate_html_records(self):
        html = '<!DOCTYPE html><html><head><title>Academic Records</title></head><body>'

        with self.lock:
            for subject, marks in self.records.items():
                html += f"<h3>{subject}</h3><ul>" + "".join(f"<li>{mark}</li>" for mark in marks) + "</ul>"
        html += '</body></html>'

        return html


if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.run()
