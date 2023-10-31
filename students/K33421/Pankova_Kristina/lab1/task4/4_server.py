
import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

names = {}
clients = []
def handle_client(client_socket, addr):
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                del names[addr]
                print(f"Connection closed with {addr}")
                break
            message = data.decode()
            print(message)
            print('\n')
            if 'Hello! My name is ' in message:
                names[addr] = message.split(' ')[4]
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())
        except (ConnectionResetError, ConnectionAbortedError) as e:
            print(f"Connection closed with {names[addr]}")
            del names[addr]
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(10)

print(f"Server started on {TCP_IP}:{TCP_PORT}")

while True:
    client_socket, addr = sock.accept()
    print(f"A new connection! Here's some info about them:")
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
