import socket
import urllib.parse



class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.grades = {}

    def serve_forever(self):
        print(f"Server started...")
        while True:
            client, addr = self.sock.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(1024).decode("utf-8")
        self.parse_request(client, data)

    def parse_request(self, client, data):
        lines = data.split("\n")
        if len(lines) < 1:
            raise HTTPError(400, 'Bad request')

        method, url, ver = lines[0].split()
        parsed_url = urllib.parse.urlparse(url)

        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')

        params = parsed_url.query.replace('=', ':').split('&')

        rq = {}
        for item in params:
            item = item.split(':')
            if len(item) > 1:
              rq[item[0]] = item[1]

        self.handle_request(client, method, rq)

    def handle_request(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.grades_to_html())
        elif method == "POST":
            discipline = params["discipline"]
            grade = params["grade"]
            if discipline in self.grades.keys():
                self.grades[discipline] = f"{self.grades[discipline]}, {grade}"
                self.send_response(client, 200, "OK", "Success!")
            else:
                self.grades[discipline] = grade
                self.send_response(client, 200, "OK", "Success!")
        else:
            raise HTTPError(404, 'Not Found', 'Method must be in ("GET", "POST")')

    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    def grades_to_html(self):
        page = "<html><body><ul>"
        for discipline, grade in self.grades.items():
            page += f"<li>{discipline}: {grade}"
        page += "</ul></body></html>"
        return page


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body

if __name__ == '__main__':

    host = 'localhost'
    port = 8080
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        serv.sock.close()
