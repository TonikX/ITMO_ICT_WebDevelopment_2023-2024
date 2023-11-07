import socket


def http_response(body: str) -> bytes:
    result = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {len(body)}\n\n{body}"
    return result.encode()


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.bind(("localhost", 9094))
conn.listen(1)

clientsocket, addr = conn.accept()
print("Received new connection from", addr)

clientsocket.sendall(http_response(open("index.html").read()))

# close connection
conn.close()
