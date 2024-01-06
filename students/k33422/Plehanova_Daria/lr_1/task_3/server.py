import socket

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        conn.listen()
        
        print(f"Server running on http://localhost:8888/")
        
        while True:
            client_conn, addr = conn.accept()
            print('Connected by', addr)
            
            with open('index.html', 'rb') as f:
                data = f.read()
            
            client_conn.sendall(
                b'HTTP/1.1 200 OK\n'
                b'Content-Type: text/html\n\n'
                + data
            )
