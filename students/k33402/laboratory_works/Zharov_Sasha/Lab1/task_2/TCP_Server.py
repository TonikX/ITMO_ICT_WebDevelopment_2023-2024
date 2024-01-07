import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(5)

timeout = 60

while True:

    server.settimeout(timeout)

    try:
        clientsocket, address = server.accept()
        print("succesfull connect!")
        msg = clientsocket.recv(1024)
        if not msg:
            break

    except socket.timeout:
        print('Time is out. {0} seconds have passed'.format(timeout))
        break


    data = msg.decode("utf-8")
    arr = data.split(" ")

    if len(arr) == 2:
        answ = int(arr[0]) * int(arr[1])
        clientsocket.send(bytes(f"Площадь параллелограмма: {answ}", "utf-8"))
    else:
        clientsocket.send(bytes("Некорректные данные", "utf-8"))

    clientsocket.close()


