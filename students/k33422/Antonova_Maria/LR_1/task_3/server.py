import socket
import threading

def handle_client(client_socket):
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    with open('index.html', 'r') as f:
        content = f.read()
    client_socket.sendall((headers + content).encode('utf-8'))
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 8080
    server.bind((host, port))
    server.listen(4)
    print(f'Started on http://{host}:{port}')
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(2048).decode('utf-8')
        print(f"-> Подключение от {address}")
        print(f"Запрос:\n{data}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()

