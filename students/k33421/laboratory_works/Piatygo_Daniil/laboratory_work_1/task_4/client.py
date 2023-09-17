import socket
import threading


def receive_message(client):
    while True:
        message = client.recv(16384).decode("utf-8")
        print(message)


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))

receive_thread = threading.Thread(target=receive_message, args=(conn,))
receive_thread.start()

while True:
    try:
        message = input()
        conn.send(message.encode("utf-8"))
    except KeyboardInterrupt:
        conn.close()
        break
