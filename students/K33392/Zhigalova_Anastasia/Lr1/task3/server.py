import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)

s.listen()

while True:
        conn, addr = s.accept()
        print('Received new connection from', addr)
        with open('index.html', 'r', encoding='utf-8') as file:
                body = file.read()
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(body)}r\n\r\n{body}"
        conn.sendall(response.encode('utf-8'))
        conn.close()
