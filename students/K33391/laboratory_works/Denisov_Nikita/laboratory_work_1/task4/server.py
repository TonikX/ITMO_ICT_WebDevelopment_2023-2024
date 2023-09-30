import socket
import threading


clients = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)


server_socket.listen(5)
print("Сервер ожидает подключения клиентов...")


def handle_client(client_socket, client_name):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            for name, socket in clients.items():
                if name != client_name:
                    socket.send(f"{client_name}: {message}".encode('utf-8'))

        except Exception as e:
            print(f"Ошибка при обработке сообщения от {client_name}: {e}")
            break

    del clients[client_name]
    print(f"{client_name} отключился.")
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент с адресом: {client_address}")

    client_name = client_socket.recv(1024).decode('utf-8')
    print(f"Клиент {client_name} присоединился к чату.")
    
    clients[client_name] = client_socket

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
    client_thread.start()
