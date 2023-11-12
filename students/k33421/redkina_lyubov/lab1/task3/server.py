import socket
import webbrowser

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)

with open("index.html", "r") as file:
    html = file.read()

while True:
    conn, addr = sock.accept()
    print(f"Подключено клиентом: {addr}")
    response = f"HTTP/1.1 200 OK\nContent-Length: {len(html)}\n\n{html}"
    conn.send(response.encode("utf-8"))
    conn.close()

webbrowser.open('http://localhost:8080')