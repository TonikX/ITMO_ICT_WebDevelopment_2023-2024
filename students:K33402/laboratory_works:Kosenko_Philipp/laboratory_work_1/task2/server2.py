import socket
def calculate_pitagoras(a, b):
    c = (a**2 + b**2) ** 0.5
    return c
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения...")
    while True:
        client_socket, addr = server_socket.accept()
        print("Подключение от:", addr)
        a = float(client_socket.recv(1024).decode())
        b = float(client_socket.recv(1024).decode())
        result = calculate_pitagoras(a, b)
        client_socket.send(str(result).encode())
        client_socket.close()
if __name__ == "__main__":
    start_server()




