import math
import pickle
import socket


def calculate_pythagoras(first_cathetus, second_cathetus):
    return math.sqrt(first_cathetus ** 2 + second_cathetus ** 2)


def init_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 9090)
    _socket.bind(server_address)

    _socket.listen(1)
    print("Wait client...")
    client_socket, client_address = _socket.accept()
    print(f"Client connected: {client_address}")

    while True:
        try:
            data = client_socket.recv(1024)
            params = eval(data.decode("utf-8"))
            if len(params) == 2:
                first_cathetus, second_cathetus = map(float, params)
                result = calculate_pythagoras(first_cathetus, second_cathetus)
                client_socket.send(str(result).encode("utf-8"))
            else:
                client_socket.send("Check your data, server receive only two args".encode("utf-8"))
        except Exception as e:
            client_socket.send(f"ERROR: {str(e)}".encode("utf-8"))
            print(f"ERROR: {str(e)}")
            break

    client_socket.close()
    _socket.close()


if __name__ == "__main__":
    init_server()
