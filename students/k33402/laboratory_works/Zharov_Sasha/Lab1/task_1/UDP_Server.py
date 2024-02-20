import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 1234))

timeout = 60

while True:
    server.settimeout(timeout)

    try:
        data = server.recvfrom(1024)

    except socket.timeout:
        print('Time is out. {0} seconds have passed'.format(timeout))
        break

    client_msg = data[0]
    addr = data[1]

    print("Clients message: " + client_msg.decode("utf-8"))

    msg = "Hello, client"
    server.sendto(msg.encode("utf-8"), addr)

server.close()