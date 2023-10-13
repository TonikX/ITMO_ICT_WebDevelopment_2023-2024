import socket
import threading
import signal

clients = {}

def handle_client(client_socket, username):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            for client, user in clients.items():
                if client != client_socket:
                    client.send(f'{username}: {message}'.encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        del clients[client_socket]
        client_socket.close()
        print(f"{username} disconnected")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1337))
    server_socket.listen(5)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print("Waiting for a connection...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        username = client_socket.recv(1024).decode('utf-8').strip()
        clients[client_socket] = username

        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

if __name__ == "__main__":
    main()
