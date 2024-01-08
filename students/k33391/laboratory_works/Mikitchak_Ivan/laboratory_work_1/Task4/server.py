import socket
import threading
import queue
import time

def handle_client(client_socket, clients, message_queue):
    # Recieve a client's login
    name = client_socket.recv(4096).decode("utf-8")

    # Register the new client
    clients.add(client_socket)

    # Serve the client until it breaks connection
    while True:
        try:
            # Recieve a message from the client
            message = client_socket.recv(4096).decode("utf-8")

            # Put the client's login concatenated with a message into the message queue
            message_queue.put(name + ": " + message)
        except:
            # Once the connection is broken remove the client
            # from the registered clients' list and exit the loop
            clients.remove(client_socket)

            break

def broadcast_messages(clients, message_queue):
    # Broadcast messages forever
    while True:
        # Check if the message queue contains new messages
        # Broadcast all messages to all registered clients
        while not message_queue.empty():
            # Extract the first message in the queue
            message = message_queue.get()

            # Send the message to all registered clients
            for client in clients:
                client.send(message.encode())

        # Set a small time delay between checks
        time.sleep(0.05)

def run_server(host, port):
    # Create a socket and put in into listening mode
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    # A clients set used to track all registered clients
    # that are in the chat
    clients = set()

    # A message queue used by broadcaster to broadcats
    # new messages to all registered clients
    message_queue = queue.Queue()

    # Start message broadcaster in a separate thread
    threading.Thread(target=broadcast_messages, args=[clients, message_queue]).start()

    # Serve clients forever
    while True:
        # Accept a client connection
        client_socket, _ = server_socket.accept()

        # Serve the client in a separate thread
        threading.Thread(target=handle_client, args=[client_socket, clients, message_queue]).start()

if __name__ == "__main__":
    host = "localhost"
    port = 5555
    run_server(host, port)
