import socket

port = 2002
data_recv = 2048
max_pending_conn = 8
host = "127.0.0.1"

#function to calculate the parallelogram area
def calc_parallelogram_area(pair):
    h, b = map(int, pair.split(" "))
    return h*b

def main():
    #Create a TCP socket and associate it with the specified IP address and port.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(max_pending_conn)

    try:
        while True:
            #Accept an incoming connection from the client.
            client, address = s.accept()

            #Receive n bytes of data from the server and decode it
            data = client.recv(port).decode("utf-8")
            print(f"Data recieved: ", data)
            result = calc_parallelogram_area(data)
            
            #Send the encoded result to client
            client.send(str(result).encode("utf-8"))
            
    except KeyboardInterrupt:
        client.close()

if __name__ == "__main__":
    main()