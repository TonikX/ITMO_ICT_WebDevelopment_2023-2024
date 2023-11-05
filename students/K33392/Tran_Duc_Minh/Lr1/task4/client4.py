import socket
import threading

port = 2002
data_recv = 2048
host = "127.0.0.1"
lock = threading.Lock()

#Function for handling incoming messages from the server
def recv_msg_handle(client):
    while True:
        #Receive a message from the server and decode it from a byte string
        msg = client.recv(data_recv).decode("utf-8")
        print(msg)

def main():
    #Create a TCP socket and establish a connection to the server.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    #Create a separate thread to receive messages from the server
    receive_thread = threading.Thread(target=recv_msg_handle, args=(s,))
    receive_thread.start()

    while True:
        try:
            #Read the message from the keyboard
            message = input()

            #Encoding it into bytes and send the message to the server
            s.send(message.encode("utf-8"))

        except KeyboardInterrupt:
            s.close()
            break

if __name__ == "__main__":
    main()
    