# Задача
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

## Реализация
1. server.py

```python
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
```

2. client.py

```python
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            incoming_message = client_socket.recv(1024).decode('utf-8')
            if not incoming_message:
                break
            else:
                print(f"-{incoming_message.strip()}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1337))

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True  # thread dies when main thread (the only non-daemon thread) exits.
    receive_thread.start()

    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == "exit":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
```

## Демонстрация работы

![task41](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/23c930f3-0468-44a3-a511-a2c45a744f0a)

![task42](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/ff072923-d338-402b-b5bc-c6b6b113857d)

![task43](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/7fea132f-f114-468f-b34e-8edf362a6692)

![task44](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/de943066-4783-4965-9ae7-f1bd87a36345)




