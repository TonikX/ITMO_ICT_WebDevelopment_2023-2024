import socket
import threading

def handle_network_inputs(client_socket):
    # Listen for incoming messages forever
    while True:
        # Recieve a new message
        message = client_socket.recv(4096).decode()

        # Print the message
        print(message)

def run_client(host, port):
    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Obtain a login from user input
    name = input("Enter your name: ")

    # Send the login to the server
    client_socket.send(name.encode())

    # Start a message listener in a separate thread
    threading.Thread(target=handle_network_inputs, args=[client_socket]).start()

    # Send messages forever
    while True:
        # Obtain a message from user input
        message = input()

        # Send the message to the server
        client_socket.send(message.encode())

if __name__ == "__main__":
    host = "localhost"
    port = 5555
    run_client(host, port)
