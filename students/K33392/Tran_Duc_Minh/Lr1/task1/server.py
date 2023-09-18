import socket

port = 2002
data_recv = 2048
msg_to_client = b"Hello client!"
host = "127.0.0.1"

def main():
    #Create a UDP socket and associate it with the specified IP address and port.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    try:
        while True:
            #Receive the data and Client address.
            msg, address = s.recvfrom(data_recv)
            print("Server reply to:", address, msg.decode("utf-8"))

            #Reply to Client
            s.sendto(msg_to_client, address)
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()