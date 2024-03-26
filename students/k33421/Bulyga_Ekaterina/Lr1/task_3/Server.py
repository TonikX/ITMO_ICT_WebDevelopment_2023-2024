from http.server import BaseHTTPRequestHandler, HTTPServer
import socket


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            with open('index.html', 'rb') as file:
                html = file.read().decode('utf-8')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404)
            return


if __name__ == '__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 9090))
    server.listen(1)
    print("Server started http://127.0.0.1:9090")

    try:
        while True:
            conn, addr = server.accept()
            print(f'Connected by {addr}')

            with open('index.html', 'rb') as file:
                html = file.read().decode('utf-8')

            conn.send(('HTTP/1.1 200 OK\nContent-Length: ' + str(len(html)) + '\n\n').encode('utf-8'))
            conn.send(html.encode('utf-8'))
    except Exception as err:
        print(err)