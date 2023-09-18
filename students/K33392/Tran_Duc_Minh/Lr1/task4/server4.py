import socket
import threading

port = 2002
data_recv = 2048
host = "127.0.0.1"
max_pending_conn = 8
lock = threading.Lock() #Synchronizing Threads
clients_list = []

def announce(msg):
    global clients_list
    for c in clients_list:
        c.send(msg.encode("utf-8"))

#Function for handling sending messages between clients.
def send_msg_handle(client, address):
    global clients_list
    while True:
        try:
            #Receive data from the client.
            msg = client.recv(data_recv).decode("utf-8")

            #Check if message is null
            if not msg:
                raise Exception

            #Send a message from the client to all other clients.
            with lock:
                for c in clients_list:
                    if c != client:
                        c.send(f"{address[1]}: {msg}".encode("utf-8"))
        except:
            tmp = clients_list
            clients_list = [i for i in tmp if i != client]
            print(f"Client {address} has left the chat")
            announce(f"Client {address[1]} has left the chat")
            break

def main():
    global clients_list

    #Create a TCP socket and associate it with the specified IP address and port.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(max_pending_conn)

    while True:
        try:
            #Accept an incoming connection from the client.
            client, address = s.accept()
            print(f"Client {address} has joined the chat")
            announce(f"Client {address[1]} has joined the chat")

            #Add the client socket to the list of clients.
            with lock:
                clients_list.append(client)
            
            #Start a separate thread to handle sending messages between clients.
            threading.Thread(target=send_msg_handle, args=(
                client, address)).start()
        except KeyboardInterrupt:
            s.close()
            break

if __name__ == "__main__":
    main()
