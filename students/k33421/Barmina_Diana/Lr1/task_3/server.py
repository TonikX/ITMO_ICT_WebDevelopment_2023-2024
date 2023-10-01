import socket


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(("127.0.0.1", 14900))
        conn.listen(10)
        while True:
            client, address = conn.accept()
            with open('index.html', 'r') as file:
                html = file.read()
            print(f"Connected by {address}")
            client.send(("HTTP/1.1 200 OK \n" + "Content-Type: text/html \n" + html).encode('utf-8'))