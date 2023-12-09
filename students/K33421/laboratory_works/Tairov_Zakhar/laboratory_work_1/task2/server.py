import math
import socket

HOST = "127.0.0.1"
PORT = 8080

VARIANT = 0

ENTRY_MSGS = [
    "Enter catheti lengths, a and b: ",
    "Enter coefficients, a, b, and c: ",
    "Enter a, b, and h: ",
    "Enter a, b, and alpha (in deg): "
]

def pythagorus(a, b):
    return ((a ** 2) + (b ** 2))

def quadratic(a, b, c):
    det = (b ** 2) - 4*a*c
    if det < 0:
        return None, None
    elif det == 0:
        return (-1 * b) / (2 * a), None
    else:
        return (-1 * b - math.sqrt(det)) / (2 * a), (-1 * b + math.sqrt(det)) / (2 * a)
    
def trapezoid(a, b, h):
    return ((a + b) / 2) * h

def parallel(a, b, alpha):
    return (a * b * math.sin(math.radians(alpha)))

OPTIONS = [pythagorus, quadratic, trapezoid, parallel]

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(20)
        server_sock.settimeout(0.5)
        while True:
            try:
                if VARIANT >= 4:
                    raise ValueError("Incorrect variant set.")
                client_sock, addr = server_sock.accept()
                client_sock.send(ENTRY_MSGS[VARIANT].encode())
                data = client_sock.recv(1024).decode()
                payload = [float(i) for i in data.split(",")]
                if VARIANT == 0:
                    if len(payload) != 2:
                        client_sock.send(b"Wrong number of arguments.")
                        continue
                    res = pythagorus(payload[0] , payload[1])
                    client_sock.send(f"Result: {res}".encode())
                else:
                    if len(payload) != 3:
                        client_sock.send(b"Wrong number of arguments.")
                        continue
                    res = OPTIONS[VARIANT](*payload)
                    client_sock.send(f"Result: {res}".encode())
            except socket.timeout:
                pass

except KeyboardInterrupt:
    exit()