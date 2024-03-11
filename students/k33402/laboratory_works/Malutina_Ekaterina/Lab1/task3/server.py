import socket


def read_html_file():
    with open('index.html', 'r') as file:
        return file.read()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1235))
server.listen(5)

while True:
    clientsocket, address = server.accept()
    html_content = read_html_file()

    response = f"""HTTP/1.1 200 OK
 Content-type: text/html
 {html_content}
 """

    clientsocket.send(response.encode('utf-8'))
    clientsocket.close()
