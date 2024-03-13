import socket

enc = "utf-8"
port = 2448
buffsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", port))

while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    data = "{} {} {}".format(a, b, c)
    s.send(data.encode(enc))
    print("Sent data to server:", data)

    response = s.recv(buffsize)
    print("Received data from server:", response.decode(enc))

    if input("Continue? Y/N: ").lower() == "n":
        break

s.close()