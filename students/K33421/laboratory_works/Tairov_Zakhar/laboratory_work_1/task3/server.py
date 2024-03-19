import contextlib
import socket

HOST = "127.0.0.1"
PORT = 8080

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(10)
        sock.settimeout(0.25)
        while True:
            with contextlib.suppress(socket.timeout):
                client_sock, addr = sock.accept()
                with open("index.html", encoding="utf-8") as index:
                    payload = index.read().encode()

                header = (
                    "HTTP/1.1 200 OK\n"
                    "Content-Type: text/html\n"
                    f"Content-Length: {len(payload)}\n"
                    "Connection: close\n\n"
                ).encode()

                client_sock.sendall(header + payload)

except KeyboardInterrupt:
    exit()
