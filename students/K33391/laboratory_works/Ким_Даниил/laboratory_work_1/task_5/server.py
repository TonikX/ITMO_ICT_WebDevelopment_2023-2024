import socket
from http.client import HTTPResponse


class HTTPServer():
    def __init__(self, host: str, port: int) -> None:
        self.Host = host
        self.Port = port
        self.Scores = {}

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind((self.Host, self.Port))
            server.listen()

            while True:
                conn, client_addr = server.accept()
                self.serve_client(conn)

        finally:
            server.close()

    def serve_client(self, conn: socket.socket):
        method, params = self.parse_request(conn)
        code, body, reason = self.handle_request(method, params)
        self.send_response(conn, code, body, reason)

    def send_response(self, conn: socket.socket, code: int, body: str, reason: str) -> None:
        resp = f'HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n'
        resp += body
        conn.send(resp.encode("utf-8"))
        conn.close()

    def parse_request(self, conn: socket.socket):
        data = conn.recv(1024).decode('utf-8')
        lines = data.split('\n')
        method, url, vers = lines[0].split()
        params = {}

        if method == 'POST':
            body = data.split('\n')[-1]

            for param in body.split('&'):
                params[param.split('=')[0]] = param.split('=')[1]

        elif method == 'GET':
            if '?' in url:
                for param in url.split('?')[1].split('&'):
                    params[param.split('=')[0]] = param.split('=')[1]

        return method, params

    def handle_request(self, method: str, params: dict):
        if method == 'POST':
            subj = params.get("subj")
            grade = params.get("grade")
            if self.Scores.get(subj):
                self.Scores[subj].append(grade)
            else:
                self.Scores[subj] = [grade]

            return 200, self.generate_html(), "OK"

        elif method == 'GET':
            return 200, self.generate_html(), "OK"

        else:
            return 404, 'Not Found'

    def generate_html(self):
        scores = [f'{subj}: {grade}' for subj, grade in self.Scores.items()]
        return '\n'.join(scores)


if __name__ == '__main__':
    server = HTTPServer("localhost", 9090)
    server.serve_forever()
