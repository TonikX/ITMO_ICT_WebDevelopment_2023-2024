import socket
import threading

from constants import HOST, INPUT_PROMPT, PORT
from utils import create_msg, recv_msg


def handle_messages(conn: socket.socket):
    while (msg := recv_msg(conn)) is not None and msg != b"":
        print(f"\n{msg.decode()}\n{INPUT_PROMPT}", end="")
    sock.close()
    print("LEAVING")


if __name__ == "__main__":
    # Init socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((HOST, PORT))

    # Create thread for handling servers' messages
    t = threading.Thread(target=handle_messages, args=(sock,))
    t.start()

    while True:
        try:
            # Get users' input and send it to the server
            sock.sendall(create_msg(input(INPUT_PROMPT)))
        except OSError:
            break
