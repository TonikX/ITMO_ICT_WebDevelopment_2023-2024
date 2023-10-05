import socket
from util.decorator import threaded


@threaded(daemon=True)
def accept(s: socket.socket):
    while True:
        data = s.recv(BUFFER_SIZE)
        if data:
            print(f"Получено сообщение: {data.decode('UTF-8')}")


if __name__ == "__main__":
    DEST = ("localhost", 1234)
    BUFFER_SIZE = 2 ** 20
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(DEST)
        accept(s)
        while True:
            try:
                inp = input()
                s.send(inp.encode("UTF-8"))
            except KeyboardInterrupt:
                break

