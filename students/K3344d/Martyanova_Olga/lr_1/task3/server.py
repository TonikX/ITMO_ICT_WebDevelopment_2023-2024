import socketserver


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


class MyHandler(socketserver.StreamRequestHandler):
    def handle(self):
        html_content = read_file('index.html')
        response = f"HTTP/1.1 200 OK\nContent-Length: {len(html_content)}\n\n{html_content}"
        self.request.sendall(response.encode('utf-8'))


if __name__ == "__main__":
    server_address = ('localhost', 8080)

    server = socketserver.TCPServer(server_address, MyHandler)
    print("Server is running... Ctrl+C to break\nCheck: http://localhost:8080/")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Connection closed")
