import socket


def create_http_request(body: str) -> bytes:
    request = f"GET /index.html HTTP/1.1\nContent-Type: text/html\nContent-Length: {len(body)}\n\n{body}"
    return request.encode()
    

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(1)

conn, addr = sock.accept()
conn.sendall(create_http_request(open("index.html").read()))
conn.close()
