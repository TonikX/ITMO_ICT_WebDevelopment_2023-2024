import socket
import sys
import threading

BUFF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8888


class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiving_thread = None
    
    def connect_to_server(self):
        try:
            self.sock.connect((self.host, self.port))
            self.receiving_thread = threading.Thread(target=self.receive_messages)
            self.receiving_thread.start()
            self.send_messages_loop()
        except ConnectionRefusedError:
            print("Cannot connect to the server.")
            self.sock.close()
            sys.exit(1)
    
    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(BUFF_SIZE).decode()
                if not message:
                    break
                print(message)
            except OSError:
                break
    
    def send_messages_loop(self):
        try:
            while True:
                message = input()
                if message:
                    self.sock.sendall(message.encode('utf-8'))
        except KeyboardInterrupt:
            print("Disconnecting from the server...")
            self.sock.close()
            sys.exit(0)


if __name__ == "__main__":
    client = ChatClient(HOST, PORT)
    client.connect_to_server()
