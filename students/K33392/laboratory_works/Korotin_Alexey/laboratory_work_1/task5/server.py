from util.http import MAPPERS, request_mapping
import socket
from json import loads


def parse_http_request(request: str):
    s = request.split("\r\n\r\n")
    if len(s) == 1:
        s.append(None)
    head, body = s
    lines = head.split("\r\n")
    method, url, version = lines[0].split()

    return method, url, body


def handle(s: socket.socket):
    data = s.recv(BUFFER_SIZE)
    request = data.decode("UTF-8")
    method, url, body = parse_http_request(request)
    if url == "/favicon.ico":
        return
    try:
        result = MAPPERS[method][url](body)
    except KeyError:
        result = "HTTP/1.0 404 NOT FOUND \n\n"
    s.send(result.encode("UTF-8"))


@request_mapping(endpoint="/grades", method="GET")
def get_mapper(body):
    with open('res/index.html', 'r') as file:
        f = file.read()

    g = list(map(lambda x: f"<tr><td>{x['subject']}</td><td>{x['description']}</td> <td>{x['grade']}</td></tr>", grades))
    f = f.replace("$grades$", "\n".join(g))
    return f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{f}'


@request_mapping(endpoint="/grades", method="POST")
def post_mapper(body):
    try:
        g = loads(body)
        grades.append(g)
        return f'HTTP/1.0 201 CREATED\n\n'
    except Exception:
        return f'HTTP/1.0 400 BAD REQUEST \n\n'


if __name__ == "__main__":
    HOST_DATA = ("localhost", 1234)
    BUFFER_SIZE = 2 ** 20
    grades = [{"subject": "123", "description": "desc", "grade": "5"}]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(HOST_DATA)
        s.listen(10)

        while True:
            try:
                client_socket, client_address = s.accept()
                handle(client_socket)
            except KeyboardInterrupt:
                break