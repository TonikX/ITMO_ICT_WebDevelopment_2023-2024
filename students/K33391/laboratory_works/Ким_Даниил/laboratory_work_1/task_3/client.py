import socket


def socket_read_all(s: socket.socket, size=1024) -> bytes:
    result = b""
    while (chunk := s.recv(size)) != b"":
        result += chunk
    return result


def read_http_body(response: bytes) -> str:
    lines = response.decode().splitlines()
    body = ""
    for i in lines:
        body += i + "\n"

    return body


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

data = socket_read_all(sock)
body = read_http_body(data)

print(body)