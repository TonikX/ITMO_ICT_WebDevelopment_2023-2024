import socket

class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.data = []

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind((self._host, self._port))
            server_socket.listen()
            while True:
                client_socket, address = server_socket.accept()
                try:
                    self.handle_client(client_socket)
                except Exception as e:
                    print('Error handling client:', e)
        finally:
            server_socket.close()

    def handle_client(self, client_socket):
        try:
            request_data = client_socket.recv(1024).decode('utf-8')
            if not request_data:
                client_socket.close()
                return
            method, url_full, headers, body_data = self.parse_request(request_data)
            response = self.handle_request(method, url_full, headers, body_data, client_socket)
            if response is not None:
                client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            error_message = f"Error: {e}"
            self.send_response(client_socket, error_message, status_code="500 Internal Server Error")
        finally:
            client_socket.close()

    def parse_request(self, request_data):
        lines = request_data.split('\r\n')
        start_line = lines[0].strip().split(" ")
        method = start_line[0]
        url_full = start_line[1]
        url_split = url_full.split('?')
        path = url_split[0]
        params = url_split[1] if len(url_split) > 1 else None
        body_data = {}
        for line in lines[1:]:
            line = line.strip()
            if not line:
                body = "\n".join(lines[lines.index(line) + 1:])
                if body:
                    parameters = body.split('&')
                    for parameter in parameters:
                        p, r = parameter.split('=')
                        body_data[p] = r
                break
        return method, path, params, body_data

    def handle_request(self, method, url_full, headers, body_data, client_socket):
        if method == "GET":
            return self.handle_get_request(url_full, client_socket)
        elif method == "POST":
            return self.handle_post_request(url_full, body_data, client_socket)
        else:
            return "Unknown Method", 405

    def handle_get_request(self, url_full, client_socket):
        if url_full == "/":
            grades_list = ""
            for value in self.data:
                grades_list += f"<li>{value['discipline']}: {value['grade']}</li>"
            with open("index.html", encoding="utf-8") as f:
                file = f.read()
            file = file.replace("GRADES", grades_list)
            self.send_response(client_socket, file)
        else:
            with open("not_found.html", encoding="utf-8") as f:
                file = f.read()
            self.send_response(client_socket, file, status_code="404 Not Found")

    def handle_post_request(self, url_full, body_data, client_socket):
        if url_full == "/add_discipline":
            discipline = body_data.get("discipline", "")
            grade = body_data.get("grade", "")
            try:
                grade = int(grade)
                if grade < 1 or grade > 5:
                    raise ValueError("Grade must be between 1 and 5")
            except ValueError:
                self.send_response(client_socket, "Invalid grade. Grade must be a number between 1 and 5",
                                   status_code="400 Bad Request")
                return
            self.data.append({"discipline": discipline, "grade": grade})
            grades_list = ""
            for item in self.data:
                grades_list += f"<tr><td>{item['discipline']}</td><td>{item['grade']}</td></tr>"
            with open("index.html", encoding="utf-8") as f:
                file = f.read()
            file = file.replace("<!-- display all disciplines and grades  -->",
                                          grades_list)
            self.send_response(client_socket, file)
        else:
            with open("not_found.html", encoding="utf-8") as f:
                file = f.read()
            self.send_response(client_socket, file, status_code="404 Not Found")

    def send_response(self, client_socket, response=None, status_code="200 OK"):
        if response is None:
            response = "Internal Server Error"
        headers = {
            "Content-Type": "text/html; charset=utf-8",
            "Connection": "close",
        }
        headers_joined = "".join(
            f"{k}: {v}\r\n" for k, v in headers.items()
        )
        client_socket.sendall(
            (
                    f"HTTP/1.1 {status_code}\r\n"
                    + headers_joined
                    + "\r\n"
                    + response
            ).encode("utf-8")
        )
if __name__ == '__main__':
    host = 'localhost'
    port = 9990
    serv = MyHTTPServer(host, port)
    try:
        serv.run()
    except KeyboardInterrupt:
        pass