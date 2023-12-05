import socket

def send_request(host, port, a, b, c):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        request = f"{a},{b},{c}"
        client_socket.sendall(request.encode())

        result = client_socket.recv(1024).decode()
        print(f"The result is: {result}")

        client_socket.close()
    except ConnectionRefusedError:
        print("Can't connect to the server")

def start_client():
    host = 'localhost'
    port = 12345

    a = input('''Enter the size of the sides. 
              You must leave one of the values blank!\nEnter cathetus A: ''')
    a = float(a) if a else None
    b = input("Enter cathetus B: ")
    b = float(b) if b else None
    c = input("Enter hypotenuse C: ")
    c = float(c) if c else None

    send_request(host, port, a, b, c)

start_client()
