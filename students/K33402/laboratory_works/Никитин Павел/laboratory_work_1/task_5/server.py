import socket

HOST_NAME = "localhost"
BUFFER = 32768
PORT = 8080


class CustomHTTPServer:
    def __init__(self, host, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connection.bind((host, port))
        self.connection.listen(5)
        self.journal = {}

    def start_server(self):
        while True:
            client, ip = self.connection.accept()
            print(ip)
            self.client_listener(client)

    def client_listener(self, client):
        data = client.recv(BUFFER).decode(encoding="utf-8", errors="ignore")
        self.parse_request(client, data)

    def parse_request(self, client, data):
        lines = data.split("\n")
        method, url, version = lines[0].split()

        if method == "GET":
            params = (
                {p.split("=")[0]: p.split("=")[1] for p in url.split("?")[1].split("&")}
                if "?" in url
                else None
            )

        elif method == "POST":
            subject = ''
            grade = ''
            print(lines)
            for line in lines:
                if 'Content-Disposition: form-data; name="subject"' in line:
                    subject = lines[lines.index(line) + 2].strip()
                elif 'Content-Disposition: form-data; name="grade"' in line:
                    grade = lines[lines.index(line) + 2].strip()

            params = {"subject": subject, "grade": grade}

        else:
            params = None

        self.response_create(client, method, params)

    def response_create(self, client, method, params):
        if method == "GET":
            self.send_response(client, 200, "OK", self.generate_html())
            print("GET 200 OK")
        elif method == "POST":
            subject = params.get("subject")
            grade = params.get("grade")
            if subject in self.journal:
                self.journal[subject].append(grade)
            else: self.journal[subject] = [grade]
            self.send_response(client, 200, "OK", f'{subject}: {grade} добавлено')
            print("POST 200 OK")
        else:
            self.send_response(client, 404, "Not Found")
            print("ERR  404")

    # noinspection PyMethodMayBeStatic
    def send_response(self, client, code, reason, body):
        response = f"HTTP/1.1 {code} {reason}\nContent-Type: text/html\n\n{body}"
        client.send(response.encode("utf-8"))
        client.close()

    def generate_html(self):
        html = "<html><body>"
        for subject in self.journal:
            html += '<div style="display: flex; flex-direction: row; gap: 5px;">'
            html += f"<div>{subject}:</div>"
            for grade in self.journal[subject]:
                html += f"<div>{grade}</div>"
            html += "</div>"
        html += "</body></html>"
        return html


if __name__ == "__main__":
    server = CustomHTTPServer(HOST_NAME, PORT)
    server.start_server()