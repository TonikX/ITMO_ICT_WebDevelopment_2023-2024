import socket
import threading

from config import BUFF_SIZE, HOST, PORT


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
        self.lock = threading.Lock()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"Server started")

            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        name = self.prompt_for_name(conn)

        if name:
            with self.lock:
                self.clients[conn] = name
            self.announce_join(name)
            try:
                while True:
                    message = conn.recv(BUFF_SIZE).decode()
                    if not message:
                        break

                    self.broadcast_message(f"{name}: {message}", conn)
            except ConnectionResetError:
                print(f"Connection reset by {name}.")
            finally:
                with self.lock:
                    if conn in self.clients:
                        del self.clients[conn]
                self.broadcast_message(f"{name} has left the chat", conn)
                conn.close()

    def prompt_for_name(self, conn):
        conn.sendall(b'Enter your name: ')
        return conn.recv(BUFF_SIZE).decode()

    def announce_join(self, name):
        print(f"New connection: {name}")
        self.broadcast_message(f"{name} joined the chat", None)

    def broadcast_message(self, message, sender_conn):
        with self.lock:
            for client_conn in self.clients:
                if client_conn != sender_conn:
                    client_conn.sendall(message.encode())

    def client_disconnect(self, name, conn):
        with self.lock:
            if conn in self.clients:
                del self.clients[conn]
        conn.close()
        self.broadcast_message(f"{name} has left the chat", None)


if __name__ == "__main__":
    chat_server = ChatServer(HOST, PORT)
    chat_server.start()
