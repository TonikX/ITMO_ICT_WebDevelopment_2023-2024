import socket
from collections import defaultdict



class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.journal = defaultdict(list)

    def socket_work(self):
        TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            TCPServerSocket.bind((self.host, self.port))
            TCPServerSocket.listen()
            while True:
                client, address = TCPServerSocket.accept()
                try:
                    self.client_work(client)
                except Exception:
                    print('Something went wrong')
        finally:
            TCPServerSocket.close()

    def client_work(self, conn):
        data = conn.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(conn, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                response = "HTTP/1.1 200 OK \n\n"
                with open('index.html', 'r') as file:
                    response += file.read()
                return response
            if method == 'POST':
                response = "HTTP/1.1 200 OK \n\n"
                parameters = body.split('&')
                sbjct, grd = [x.split('=')[1] for x in parameters]
                self.journal[sbjct].append(grd)

                response += "<html><head><title>Journal</title></head><body><ol>"
                response += "<pre>"
                response += f"<b>Subject{' '*10}Grades</b>"
                for sbjct, grd in self.journal.items():
                    response += f"<p>{sbjct}{' '*(10+7-len(sbjct))}{','.join(grd)}</p>"
                response += "</pre>"
                response += '<a href="/">Go back to submitting grades</a>'
                response += "</ol></body></html>"
                return response

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = 'localhost'
    port = 9090
    serv = MyHTTPServer(host, port)
    try:
        serv.socket_work()
    except KeyboardInterrupt:
        pass