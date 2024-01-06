# Задание 4

## Описание Задачи

Задание включает в себя разработку многопользовательского чата. Целью является создание серверной и клиентской части
приложения, где клиенты могут подключаться к серверу и обмениваться сообщениями. Важно использовать
библиотеку `threading` для обработки множественных клиентских соединений и передачи сообщений в реальном времени.

## Реализация

### Серверная Часть

Файл: `server.py`

Сервер создает TCP-сокет и ожидает подключений от клиентов. При подключении клиента сервер запрашивает имя и начинает
принимать сообщения от клиента, рассылая их всем подключенным клиентам.

```python
import socket
import threading

BUFF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8888


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
            
            print(f"Chat Server running on {self.host}:{self.port}")
            
            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()
    
    def handle_client(self, conn, addr):
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
```

### Клиентская Часть

Файл: `client.py`

Клиент подключается к серверу, отправляет и получает сообщения. Каждый клиент имеет возможность отправлять сообщения,
которые будут видны всем подключенным клиентам.

```python
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
```

## Выводы

Реализованный чат демонстрирует возможности многопоточности и сетевого программирования в
Python. Применение TCP обеспечивает надежную доставку сообщений, а `threading` позволяет эффективно обрабатывать
множество клиентских соединений.