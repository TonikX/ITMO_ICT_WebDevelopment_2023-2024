import socket
def start_client():
    server_address = ('localhost', 1234)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    client_socket.send(str(a).encode())
    client_socket.send(str(b).encode())
    result = float(client_socket.recv(1024).decode())
    print("Результат:", result)
    client_socket.close()

if __name__ == "__main__":
    start_client()
