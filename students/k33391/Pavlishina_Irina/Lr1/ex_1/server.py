import socket
import threading

"""
    UDP server code
    Can recieve messages and send responces on port 8080 of lockalhost, creating different thread for each client.  
    
"""
PORT = 8080


def recieve(data):
    """

    :param data: [ <client message>, <client_address>,  <client_socket> ]
    :return: Nothing
    """
    print(data[0])
    data[2].sendto(b"Hello, client", data[1])


def main():
    """
    Main function of code server running
    Bind to the port and listen it. After recieving create thread and send response.

    :return: Nothing
    """
    global PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        thread = threading.Thread(target=recieve, args=([data, addr, sock],))
        thread.start()


if __name__ == "__main__":
    main()