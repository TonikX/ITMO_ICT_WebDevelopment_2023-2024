
import collections
import json
import socket
import typing as tp
import urllib.parse

class HTTPException(Exception):
    def __init__(self, code: int, explain: str):
        self.code = code
        self.explain = explain

class GradesHTTPServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def serve_forever(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen(20)
            while True:
                client_sock, _ = sock.accept()
                with client_sock:
                    self.serve_client(client_sock)

    def serve_client(self, sock: socket.socket):
        request = sock.recv(1024).decode()
        try:
            method, path = self.parse_request(request)
            body = self.parse_body(request)
            self.handle_request(sock, method, path, body)
        except HTTPException as e:
            self.send_response(sock, self.error_html_generator(e.code, e.explain), 
                               e.code)
        
    @staticmethod
    def parse_request(request: str) -> tp.Tuple[str, str, tp.Dict[tp.Any, tp.Any]]:
        lines = request.split("\r\n")
        if len(lines) < 1:
            raise HTTPException(400, "Bad Request")
        method, url, ver = lines[0].split()
        if ver != "HTTP/1.1":
            raise HTTPException(505, "HTTP Version Not Supported")
        parse_res = urllib.parse.urlparse(url)

        return method, parse_res.path
    
    @staticmethod
    def parse_headers(request: str) -> tp.Dict[str, str]:
        lines = request.split("r\n")
        headers = {}
        for line in lines[1:]:
            if line == "":
                break
            key, value = line.split(": ")
            headers[key] = value
        return headers
    
    @staticmethod
    def parse_body(request: str) -> str:
        lines = request.split("\r\n")
        gap_idx = lines.index("")
        if len(lines) > gap_idx + 1:
            return "\n".join(lines[gap_idx + 1:])
        return ""

    def handle_request(self, sock, method, path, body):
        if path != "/":
            raise HTTPException(404, "Not Found")
        if method == "GET":
            with open("grades.json", encoding="utf-8") as f:
                grades = json.loads(f.read())
            self.send_response(sock, self.grades_body_generator(grades))
        elif method == "POST":
            grades = json.loads(body)
            with open("grades.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(grades))
            self.send_response(sock, "")
        else:
            raise HTTPException(405, "Method Not Allowed")

    def send_response(self, sock, body, code=200):
        response = f"""HTTP/1.1 {code}
Content-Type: text/html; charset=utf-8
Content-Length: {len(body.encode("utf-8"))}

{body}
"""
        sock.send(response.encode("utf-8"))

    @staticmethod
    def error_html_generator(code, explain):
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{explain}</title>
</head>
<body>
{code} {explain}
</body>
</html>
"""
    
    @staticmethod
    def grades_body_generator(grades):
        body = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Grades</title>
</head>
<body>
<ul>
"""
        for discipline, grade in grades.items():
            body += f"<li>{discipline}: {grade}"
        body += """
</ul>
</body>
</html>
"""
        return body

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    server = GradesHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        exit()
