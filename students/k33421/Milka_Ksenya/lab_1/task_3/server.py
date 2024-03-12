import socket

from config import HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on http://{HOST}:{PORT}/")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)

        with open('index.html', 'rb') as f:
            data = f.read()

        conn.sendall(
            b'HTTP/1.1 200 OK\n'
            b'Content-Type: text/html\n\n'
            + data
        )
