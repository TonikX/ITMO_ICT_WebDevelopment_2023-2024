import json
import socket
import urllib.parse


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.grades = {}

    def serve_forever(self):
        print(f"Server is listening on http://{self.host}:{self.port}")
        while True:
            client, addr = self.socket.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(16384).decode("utf-8")
        if not data:
            client.close()
            return
        self.parse_request(client, data)

    def parse_request(self, client, data):
        lines = data.split("\n")
        if len(lines) < 1:
            self.send_response(client, 400, "Bad Request", "Invalid request")
            client.close()
            return

        request_line = lines[0].split()
        if len(request_line) != 3:
            self.send_response(client, 400, "Bad Request", "Invalid request line")
            client.close()
            return

        method, url, version = request_line
        parsed_url = urllib.parse.urlparse(url)
        print(data)
        params = data.split("\r\n\r\n")[1]
        self.handle_request(client, method, params)

    def handle_request(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.grades_to_html())
        elif method == "POST":
            params = json.loads(params)
            discipline = params.get("discipline")
            grade = params.get("grade")
            if discipline and grade:
                if discipline in self.grades:
                    existing_grades = self.grades[discipline]
                    self.grades[discipline] = f"{existing_grades}, {grade}"
                else:
                    self.grades[discipline] = grade
                self.send_response(client, 200, "OK", "Saved!")
            else:
                self.send_response(
                    client, 400, "Bad Request", "Discipline and grade are required."
                )
        else:
            self.send_response(client, 404, "Not Found", "Incorrect method.")

    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    def grades_to_html(self):
        grade_list = "".join(
            [f"<li>{discipline}: {grade}" for discipline, grade in self.grades.items()]
        )
        return f"<html><body><ul>{grade_list}</ul></body></html>"


if __name__ == "__main__":
    host = "localhost"
    port = 6660
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
