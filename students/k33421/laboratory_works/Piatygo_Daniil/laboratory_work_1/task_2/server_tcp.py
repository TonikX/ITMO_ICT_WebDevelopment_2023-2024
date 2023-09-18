import socket


def calculate(cathetus_1, cathetus_2=None, hypotenuse=None):
    if cathetus_2 is None and hypotenuse is None:
        return "Invalid input"
    if hypotenuse and cathetus_1 >= hypotenuse:
        return "Triangle does not exist"
    if cathetus_2 is None:
        return (hypotenuse**2 - cathetus_1**2) ** 0.5
    if hypotenuse is None:
        return (cathetus_1**2 + cathetus_2**2) ** 0.5
    return "Something went wrong"


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen()

conn, addr = conn.accept()
while True:
    data = conn.recv(1024).decode("utf-8")
    if not data:
        break
    operation, a, b = data.split()
    a, b = float(a), float(b)
    if operation == "hypotenuse":
        result = calculate(cathetus_1=a, cathetus_2=b)
    elif operation == "cathetus":
        result = calculate(cathetus_1=a, hypotenuse=b)
    else:
        result = "Invalid operation"
    conn.send(bytes(str(result), encoding="utf-8"))
