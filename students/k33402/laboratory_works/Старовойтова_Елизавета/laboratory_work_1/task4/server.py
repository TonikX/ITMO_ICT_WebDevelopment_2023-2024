import socket
import threading

host = "127.0.0.1"
port = 59000
buffSize = 1024

tcpServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServerSock.bind((host, port))
tcpServerSock.listen()
clients = []
aliases = []


# func which send messages for all clients
def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode("utf-8"))
            aliases.remove(alias)
            break


def receive():
    while True:
        print("Server is running and listening....")
        client, address = tcpServerSock.accept()
        print(f'Connection is established with {str(address)}')
        client.send("alias?".encode("utf-8"))
        alias = client.recv(buffSize).decode("utf-8")
        aliases.append(alias)
        clients.append(client)
        print(f"The alias of this client is {alias}".encode("utf-8"))
        broadcast(f"{alias} has connected to the chat room!".encode("utf-8"))
        client.send("You're now connected!".encode("utf-8"))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
