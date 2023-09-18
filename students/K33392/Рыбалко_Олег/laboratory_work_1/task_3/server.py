import socket


def create_http_response(body: str) -> bytes:
    request = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {len(body)}\n\n{body}"
    return request.encode()
    

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9090))
sock.listen(1)

conn, addr = sock.accept()
conn.sendall(create_http_response(open("index.html").read()))
conn.close()
