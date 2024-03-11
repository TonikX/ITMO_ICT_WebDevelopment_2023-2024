import socket
from math import sqrt


def pyth_theorem(cath1, cath2=None, hyp=None):
    if not (cath1 or hyp) or (hyp and cath1 >= hyp):
        return "Invalid input"
    if not cath2:
        return sqrt(hyp ** 2 - cath1 ** 2)
    if not hyp:
        return sqrt(cath1 ** 2 + cath2 ** 2)
    return "Something went wrong"


if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 6999

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((server_ip, server_port))
    conn.listen()

    conn, addr = conn.accept()
    while True:
        data = conn.recv(1024).decode("utf-8")

        if not data:
            continue

        operation, a, b = data.split(',')
        a, b = float(a), float(b)

        if operation == "hyp":
            result = pyth_theorem(cath1=a, cath2=b)
        elif operation == "cath":
            result = pyth_theorem(cath1=a, hyp=b)
        else:
            result = "Invalid operation"

        conn.send(bytes(str(result), encoding="utf-8"))
