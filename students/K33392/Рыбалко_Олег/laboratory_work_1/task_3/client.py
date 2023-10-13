import socket


def socket_read_all(s: socket.socket, chunk_size=1024) -> bytes:
    result = b""
    while (chunk := s.recv(chunk_size)) != b"":
        result += chunk
    return result


def read_http_body(response: bytes) -> str:
    lines = response.decode().splitlines()
    body_start = next((i for i, line in enumerate(lines) if line == ""), -1)
    if body_start == -1:
        raise ValueError("invalid http response")
    return "\n".join(lines[body_start + 1:])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

data = socket_read_all(sock)
body = read_http_body(data)

print(body)
