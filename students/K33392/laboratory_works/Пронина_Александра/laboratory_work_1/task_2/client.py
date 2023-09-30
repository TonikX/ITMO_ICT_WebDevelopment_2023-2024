import socket


def send_request(operate, params):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    request = operate + ' ' + ' '.join(params)
    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()

    client_socket.close()

    return response


operation = input("Введите код операции (a, b, c или d): ")
parameters = input("Введите параметры через пробел: ").split()

result = send_request(operation, parameters)

print("Результат:", result)
