import socket
import threading

if __name__ == "__main__":
    clients_list = []
    lock = threading.Lock()

    server_ip = "127.0.0.1"
    server_port = 3003

    def send_message_handler(client, addr, clients_list):
        while True:
            data = client.recv(1024).decode("utf-8")
            if not data:
                break
            with lock:
                for c in clients_list:
                    if c != client:
                        c.send(f"{addr[1]}: {data}".encode("utf-8"))

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conn.bind((server_ip, server_port))
    conn.listen(10)

    while True:
        try:
            print("Waiting for a connection...")
            client, addr = conn.accept()
            print(f"Accepted connection from {addr}")
            with lock:
                clients_list.append(client)
            threading.Thread(target=send_message_handler, args=(client, addr, clients_list)).start()
        except KeyboardInterrupt:
            conn.close()
            break