import socket
import sys

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self.marks = {}

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.bind((self._host, self._port))
            sock.listen()

            while True:
                conn, _ = sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print("Client servering failed", e)
        finally:
            sock.close()

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            print(req.method)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            print("error")
            # self.send_error(conn, e)
        if conn:
            conn.close()

    def parse_request(self, conn):
        rfile = conn.makefile("rb")
        method, url, version = self.parse_request_line(rfile)
        print(method, url, version)
        headers = self.parse_headers(rfile)
        adress, parameters = self.parse_url(url)
        print(adress, parameters)
        return Request(method, url, adress, parameters, version, headers, rfile)

    def parse_url(self, url):
        try:
            adress, parametersarr = url.split("?")
            parametrs = {}
            parametersarr = parametersarr.split("&")
            for parameter in parametersarr:
                nameparameter, valueparameter = parameter.split("=")
                parametrs[nameparameter] = valueparameter
            return adress, parametrs
        except:
            return url, ""

    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise Exception("Request line is too long")
        req_line = str(raw, "iso-8859-1")
        req_line = req_line.rstrip("\r\n")
        words = req_line.split()
        if len(words) != 3:
            raise Exception("Malformed request line")
        method, target, ver = words
        if ver != "HTTP/1.1":
            raise Exception("Unexpected HTTP version")
        return method, target, ver

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception("Header line is too long")

            if line in (b"\r\n", b"\n", b""):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise Exception("Too many headers")
            return headers

    def handle_request(self, req):
        if req.method == "POST":
            return self.handle_post(req)
        if req.method == "GET":
            return self.handle_get(req)
        else:
            return Response(404, "Not found")

    def handle_post(self, req):
        id = len(self.marks) + 1
        self.marks[id] = {
            "id": id,
            "discipline": req.parameters["discipline"],
            "marks": req.parameters["marks"],
        }
        return Response(200, "Created")

    def handle_get(self, req):
        print("FUNC GET")
        contentType = "text/html; charset=utf-8"
        body = "<html><head></head><body>"
        body += f"<div>Отметки ({len(self.marks)})</div>"
        body += "<ul>"
        for u in self.marks.values():
            body += f'<li>#{u["id"]} {u["discipline"]}, {u["marks"]}</li>'
        body += "</ul>"
        body += "</body></html>"
        body = body.encode("utf-8")
        headers = [("Content-Type", contentType), ("Content-Length", len(body))]
        return Response(200, "OK", headers, body)

    def send_response(self, conn, resp):
        wfile = conn.makefile("wb")
        status_line = f"HTTP/1.1 {resp.status} {resp.reason} \r\n"
        wfile.write(status_line.encode("iso-8859-1"))

        if resp.headers:
            for key, value in resp.headers:
                header_line = f"{key}: {value}\r\n"
                wfile.write(header_line.encode("iso-8859-1"))

        wfile.write(b"\r\n")

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()


class Request:
    def __init__(
        self, method, url, adress, parameters, version, headers, rfile
    ) -> None:
        self.method = method
        self.target = url
        self.version = version
        self.headers = headers
        self.rfile = rfile
        self.adress = adress
        self.parameters = parameters


class Response:
    def __init__(self, status, reason, headers=None, body=None) -> None:
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body

# Для запуска программы нужно ввести в терминале python3 server.py host(127.0.0.1) port(53210) name(example.local)

# Для подключения к серверу нужно ввести nc localhost порт(53210)

# Для добавления новых оценок нужно ввести POST /marks?discipline={name_discipline}&marks={mark} HTTP/1.1

# Для получения всех оценок нужно ввести GET /marks HTTP/1.1

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
