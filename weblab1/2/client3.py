import socket


def receive_message():
    message = socket.recv(128).decode()
    print(message)


server_address = ('localhost', 55555)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server_address)

receive_message()

while True:
    msg = input()
    socket.send(msg.encode())
    if msg == 'exit':
        break
    elif msg == 'Find equation roots':
        receive_message()

        coefficients = input()
        socket.send(coefficients.encode())
        receive_message()
    else:
        receive_message()

socket.close()
