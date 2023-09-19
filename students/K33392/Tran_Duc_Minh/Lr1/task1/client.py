import socket

port = 2002
data_recv = 2048
msg_to_sv = b"Hello server!"
host = "127.0.0.1"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #associate with the specified IP address and port.
    s.connect((host, port))
    
    try:
        #Send message to the server
        s.send(msg_to_sv)

        #Receive n bytes of data from the server
        msg, address = s.recvfrom(data_recv)
        print(msg.decode("utf-8"))
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()