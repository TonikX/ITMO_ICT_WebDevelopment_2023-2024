import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('localhost', 7777)

conn.bind(server_adress)
conn.listen(1)
print(f"Server is running on http://{server_adress[0]}:{server_adress[1]}")

def send_response(sock):
    with open('index.html', 'rb') as f:
        content = f.read()
        resp = b"HTTP/1.1 200 OK\r\n Content-Type: text/html\r\n"
        resp += b"Content-Length: " + str(len(content)).encode() + b"\r\n"
        resp += b"\r\n"
        resp += content

        sock.send(resp)

while True:
    sock, adr = conn.accept()
    print(f"Connection from {adr}")
    request = sock.recv(1024)
    print(request.decode())

    send_response(sock)
    sock.close()