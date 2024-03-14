import socket


class MyHTTPServer:
    def __init__(self):

        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind(("localhost", 9089))
        self.conn.listen(5)
        self.marks = {}

    def serve_forever(self):
        while True:
            client_socket, addr = self.conn.accept()
            self.serve_client(client_socket)

    def serve_client(self, client):
        data = client.recv(1024).decode()
        self.parse_request(client, data)

    def parse_request(self, client, data):
        body = data.split("\n")
        method, url, version = body[0].split()
        params = {}
        if method == "GET":
            if "?" in url:
                args = url.split("?")[1].split("&")
                for arg in args:
                    key, value = arg.split("=")
                    params[key] = value
            else:
                params = None

        elif method == "POST":
            body = data.split("\n")[-1]
            args = body.split("&")
            for arg in args:
                key, value = arg.split("=")
                params[key] = value

        self.handle_request(client, method, params)

    def handle_request(self, client, method, params):
        if method == "GET":
            if params is None:
                self.send_response(client, 200, "OK", self.generate_html())
            else:
                self.send_response(client, 200, "OK", self.generate_html(subject=params.get("subject")))
            print("GET 200 OK")
        elif method == "POST":
            discipline = params.get("subject")
            mark = params.get("mark")
            try:
                self.marks[discipline].append(mark)
            except:
                self.marks[discipline] = [mark]
            self.send_response(client, 200, "OK", f'{discipline}: {mark} добавлено')
            print("POST 200 OK")
        else:
            self.send_response(client, 404, "Not Found")
            print("ERR  404")

    def send_response(self, client, code, reason, body=None):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    def generate_html(self, subject=None):

        if subject is None:
            lines = []
            for discipline, mark in self.marks.items():
                lines.append(f"{discipline}: {' '.join(mark)}<br>")

            page = (
                "<html><body><div>"
                f"{''.join(lines)}"
                "</div></body></html>"
            )
        else:
            marks = ' '.join(self.marks.get(subject))
            page = (
                "<html><body><div>"
                f"{''.join([f'<p>{subject}: {marks}</p>'])}\n"
                "</div></body></html>"
            )
        return page


if __name__ == "__main__":
    server = MyHTTPServer()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.conn.close()
