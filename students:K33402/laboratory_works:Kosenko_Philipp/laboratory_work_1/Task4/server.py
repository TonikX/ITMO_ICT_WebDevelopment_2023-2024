from socket import *
from threading import Thread

class Server:
    host = 'localhost'
    port = 10000
    client_sockets = set()
    separator_token = "<SEP>"

    def __init__(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        self.socket = server_socket

    def run(self):
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"[+] {client_address} connected.")
            self.client_sockets.add(client_socket)

            t = Thread(target=self._recieve_message, args=(client_socket,))
            t.daemon = True
            t.start()

    def _recieve_message(self, cs):
        while True:
            try:
                msg = cs.recv(1024).decode()
            except Exception as e:
                print(f"[!] Error: {e}")
                self.client_sockets.remove(cs)
            else:
                msg = msg.replace(self.separator_token, ": ")
            for client_socket in self.client_sockets:
                client_socket.send(msg.encode())


if __name__ == "__main__":
    server = Server()
    server.run()