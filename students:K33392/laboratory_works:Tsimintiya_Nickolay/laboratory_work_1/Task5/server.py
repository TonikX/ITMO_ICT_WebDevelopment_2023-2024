import socket
import sys
from k import *
from request import Request
from response import Response

class MyHTTPServer:
    def __init__(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind((host, port))
        self.conn.listen()
        self.disciplines = {}

    def serve_forever(self):
        while True:
            client, addr = self.conn.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(1024).decode("utf-8")
        request = self.parse_request(client, data)
        result = self.handle_request(request)
        self.send_response(request.client, result)

    def parse_request(self, client, data):
        lines = data.split("\n")
        method, url, version = lines[0].split()
        params = (
            {p.split("=")[0]: p.split("=")[1] for p in url.split("?")[1].split("&")}
            if "?" in url
            else None
        )
        request = Request(client, method, params)
        return request

    def handle_request(self, request):
        client, method, options = request.client, request.method, request.options

        if method == K.getMethod():
            return Response(200, K.Responses.ok(), self.grades_to_html())

        if method == K.postMethod():
            discipline = options.get("discipline")
            new_grade = options.get("grade")

            grades = self.disciplines.get(discipline, None)
            if (grades):
                self.disciplines[discipline].append(new_grade)
            else:
                self.disciplines[discipline] = [new_grade]

            return Response(200, K.Responses.ok(), "Saved")

    def send_response(self, client, result):
        response = f"HTTP/1.1 {result.code} {result.info}\nContent-Type: text/html\n\n{result.body}"
        client.send(response.encode("utf-8"))
        client.close()

    def grades_to_html(self):
        page = (
            f"<html><body><ul>"
            f"{''.join([f'<li>{discipline}: {grade}' for discipline, grade in self.disciplines.items()])}"
            f"</ul></body></html>"
        )
        return page


if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.conn.close()