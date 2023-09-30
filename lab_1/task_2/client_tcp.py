import socket

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    inp_string = input("Enter the length of two legs: ").encode(codage)
    client_socket.send(inp_string)

    result = client_socket.recv(1024).decode(codage)

    print(f"Hypotenuse length: {result}")

    client_socket.close()


if __name__ == "__main__":
    main()