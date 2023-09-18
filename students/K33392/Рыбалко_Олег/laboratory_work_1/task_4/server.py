import os
import socket
import struct
import threading

from constants import HOST, PORT, WELCOME_MESSAGE
from utils import recv_msg, create_msg


def handle_client(conn: socket.socket, addr: tuple):
    try:
        while (msg := recv_msg(conn)) is not None and msg != b"quit":
            send_message_to_clients(msg, addr)
    finally:
        conn.close()


def send_message_to_clients(msg: bytes, addr: tuple):
    global connections

    payload = create_msg(f"{addr[0]}:{addr[1]}: ".encode() + msg + b"\n")

    # Send message to all connected users
    indexes = set()
    for i, (conn, conn_addr) in enumerate(connections):
        if addr == conn_addr:
            continue
        try:
            conn.send(payload)
        except OSError:
            indexes.add(i)

    # Remove disconnected users
    indexes = list(indexes)
    indexes.reverse()
    for i in indexes:
        connections.pop(i)


def handle_connections(sock: socket.socket):
    print("Server listening on", HOST, "port", PORT)

    while True:
        # Accept client connections
        conn, addr = sock.accept()
        print("New connection", addr)

        conn.send(WELCOME_MESSAGE)

        send_message_to_clients(f"New user has joined: {addr}".encode(), ("Server", ""))

        connections.append((conn, addr))

        # Create a new thread to handle the client
        client_thread = threading.Thread(
            target=handle_client,
            args=(
                conn,
                addr,
            ),
        )
        client_thread.start()


if __name__ == "__main__":
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(os.cpu_count())

    # Create array for storing active connections
    connections: list[socket.socket] = []

    handle_connections(sock)