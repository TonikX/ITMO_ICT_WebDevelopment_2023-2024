import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 9090))

try:
    m = float(input("Введите размер средней линии трапеции: "))
    client.send(str(m).encode())
    h = float(input("Введите высоту трапеции: "))
    client.send(str(h).encode())

    res, addr = client.recvfrom(1024)

    print(f"Площадь трапеции: {res.decode()}")

    client.close()
except Exception as e:
    print(e)

