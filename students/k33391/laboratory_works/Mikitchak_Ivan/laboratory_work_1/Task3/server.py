import socket

def tcp_server(host, port):
    # Create a server socket and put it into listening mode
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()

        # Open the index page file
        f = open("Lab1/Task3/index.html")

        # Send file's content to the client
        client_socket.send(f.read().encode())

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 5555
    tcp_server(host, port)