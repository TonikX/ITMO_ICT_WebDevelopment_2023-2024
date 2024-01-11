import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7777)
sock.connect(server_address)

http_request = f"GET / HTTP/1.1\r\nHost: http://{server_address[0]}:{str(server_address[1])}\r\n\r\n"
sock.send(http_request.encode('utf-8'))

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

sock.close()