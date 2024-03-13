import socket
import json

def tcp_client(host, port):
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Read quadratic equation parameters from user input
    parameters = read_parameters()

    # Convert parameters into a json object
    json_string = json.dumps(parameters)

    # Send json object to the server
    client_socket.send(json_string.encode())

    # Receive a message from the server
    data = client_socket.recv(1024).decode()

    # Parse the message
    # The message is a json object containing
    # a list of solutions
    solutions = json.loads(data)

    # Print solutions
    print(solutions)

    # Close the connection
    client_socket.close()

def read_parameters():
    while True:
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
        except Exception:
            print("All values should be numerical. Try again.")
            continue
        break
    return (a, b, c)

if __name__ == '__main__':
    host = 'localhost'
    port = 5555
    tcp_client(host, port)