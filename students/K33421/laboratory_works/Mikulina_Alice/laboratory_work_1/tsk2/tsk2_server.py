import socket

def calculate_side(a, b, c):
    if a is None:
        return (c ** 2 - b ** 2) ** 0.5    
    elif b is None:
        return (c ** 2 - a ** 2) ** 0.5    
    elif c is None:
        return (a ** 2 + b ** 2) ** 0.5

def handle_client(connection):
    data = connection.recv(1024).decode()
    params = data.split(',')
    if len(params) != 3:
        connection.send(b"Invalid parameters")
    else:
        try:
            a = float(params[0]) if params[0] != "None" else None 
            b = float(params[1]) if params[1] != "None" else None 
            c = float(params[2]) if params[2] != "None" else None 
            result = calculate_side(a, b, c)
            connection.send(str(result).encode())
        except ValueError:
            connection.send(b"Invalid parameters")

    connection.close()

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server started. Waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection established from {address[0]}:{address[1]}")
        
        handle_client(client_socket)

start_server()