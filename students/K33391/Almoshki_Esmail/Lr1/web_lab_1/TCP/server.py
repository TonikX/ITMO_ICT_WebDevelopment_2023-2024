import math
import socket, threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234
FORMAT = "utf-8"
ADDRESS = (SERVER, PORT)
HEADER = 64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def start_server():
    server.listen()
    print(f"[starting] Server is running on {SERVER}")
    while True:
        client_socket, address = server.accept()
        # print(f"[Connected] client with address {address} connected")
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()


def handle_client(client_socket, address):
    print(f"[NEW CONNECTION]new connection from address {address}")

    msg = client_socket.recv(HEADER).decode(FORMAT)
    print(f"{address}  {msg}")
    numbers_array = msg.split(" ")

    client_socket.send(getequationroot(numbers_array).encode(FORMAT))


def getequationroot(array):
    # reformat data type [cast to integer]
    for i in range(len(array)):
        array[i] = int(array[i])
    A = array[0]
    B = array[1]
    C = array[2]

    delta = pow(B,2) - 4*A*C

    if A == 0:
        if B == 0:
            if C == 0:
                return "The equation is always valid"
            else:
               return "The equation is always invalid"
        else:
            return f'answer is {-C / B}'



    if delta < 0:
        return f"There is no real root for this equation"

    elif delta == 0:
        answer = (-B / 2 * A)
        return f"the answer is {answer}"

    else:
        first_root = (-B + math.sqrt(delta))/2*A
        second_root = (-B - math.sqrt(delta)) / 2 * A
        return f"Solutions are ({first_root}, {second_root})"




start_server()
