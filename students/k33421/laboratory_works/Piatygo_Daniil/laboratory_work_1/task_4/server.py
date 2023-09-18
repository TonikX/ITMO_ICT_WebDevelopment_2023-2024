import socket
import threading


clients = []
lock = threading.Lock()


def send_message(client, addr):
    while True:
        data = client.recv(16384).decode("utf-8")
        if not data:
            break
        with lock:
            for c in clients:
                if c != client:
                    c.send(f"{addr[1]}: {data}".encode("utf-8"))


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn.bind(("127.0.0.1", 8000))
conn.listen(5)

while True:
    try:
        client, addr = conn.accept()
        with lock:
            clients.append(client)
        threading.Thread(target=send_message, args=(client, addr)).start()
    except KeyboardInterrupt:
        conn.close()
        break
