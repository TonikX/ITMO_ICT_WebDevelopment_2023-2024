import socket

if __name__ == "__main__":
    DEST = ("localhost", 1234)
    BUFFER_SIZE = 2 ** 20

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hello from client", DEST)
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        decoded = data.decode("UTF-8")
        print(decoded)
