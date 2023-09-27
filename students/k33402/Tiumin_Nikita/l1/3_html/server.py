import socket


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()

        request_data = conn.recv(1024)

        with open('C:\\Users\\tyumi\\Desktop\\web\\students\\k33402\\Tiumin_Nikita\\l1\\3_html\\index.html', 'r') as f:
            html = f.read()

        conn.send(encode('HTTP/1.0 200 OK\n'))
        conn.send(encode('Content-Type: text/html\n'))
        conn.send(encode('\n'))
        conn.send(encode(html))

        conn.close()


def encode(msg):
    return msg.encode('utf-8')


if __name__ == '__main__':
    run()
