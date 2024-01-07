import socket

FORMAT = 'utf-8'
PORT = 8888
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()

while True:
    client_conn, address = server.accept()
    client_conn.recv(1024)

    response_type = "HTTP/1.0 200 OK\n"
    headers =  "text/html\n\n"

    body = '''
    <html>
        <body>
            <H1> Heloo World! <H1>
        </body>
    </html>
    '''

    response = response_type + headers + body
    client_conn.send(response.encode(FORMAT))

    client_conn.close()

