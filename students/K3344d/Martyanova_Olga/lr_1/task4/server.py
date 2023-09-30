import signal
import socket
import sys
import threading

clients = []


def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                clients.remove(client_socket)
                break
            address = client_socket.getpeername()

            message = f"{address}: {data.decode('utf-8')}"
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break


def signal_handler(sig, frame):
    for client in clients:
        client.close()
    server_socket.close()
    print('\nServer closed')

    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12342)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server is running. Waiting for a clients...")

while True:
    try:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Welcome {client_address}")
        client_handler = threading.Thread(target=handle_client,
                                          args=(client_socket,))
        client_handler.daemon = True
        client_handler.start()
    except KeyboardInterrupt:
        server_socket.close()
        break
