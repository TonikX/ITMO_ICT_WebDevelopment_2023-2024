import socket

def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12124)
    server_socket.bind(server_address)

    server_socket.listen(1)
    print("Сервер ожидает подключения...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключено клиентом: {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено от клиента: {data}")

        a, b = map(int, data.split(','))

        result = calculate_hypotenuse(a, b)

        client_socket.send(str(result).encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
