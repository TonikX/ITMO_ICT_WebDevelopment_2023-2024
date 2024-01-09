import socket

host = '127.0.0.1'
port = 14560
bufferSize = 1024


class MyHTTPServer:
    def __init__(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.conn.bind((host, port))
        self.conn.listen(10)
        self.grades = {}

    def start_server(self):
        while True:
            client, address = self.conn.accept()
            self.listen_client(client)

    def listen_client(self, client):
        data = client.recv(bufferSize).decode("utf-8")
        self.parse_request(client, data)

    def parse_request(self, client, data):
        lines = data.split('\n')
        method, url, vers = lines[0].split()

        if method == 'POST':
            body = data.split('\n')[-1]
            params = {p.split('=')[0]: p.split('=')[1] for p in body.split('&')}

        elif method == 'GET':
            params = (
                {p.split('=')[0]: p.split('=')[1] for p in url.split('?')[1].split('&')}
                if '?' in url
                else None
            )
        else:
            params = None

        self.create_response(client, method, params)

    def create_response(self, client, method, params):
            if method == 'POST':
                subj = params.get("subj")
                grade = params.get("grade")
                self.grades[subj] = grade
                self.send_response(client, 200, self.generate_html(), "OK")
                print('POST 200 OK')
            elif method == 'GET':
                self.send_response(client, 200, self.generate_html(), "OK")
                print('GET 200 OK')
            else:
                self.send_response(client, 404, 'Not Found')
                print('Error 404')

    def send_response(self, client, code, body, reason):
            resp = f'HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n'
            resp += body
            client.send(resp.encode("utf-8"))
            client.close()


    def generate_html(self):
            grades_list = [f'{subj}: {grade}' for subj, grade in self.grades.items()]
            return '\n'.join(grades_list)


if __name__ == '__main__':
    server = MyHTTPServer(host, port)
    server.start_server()
