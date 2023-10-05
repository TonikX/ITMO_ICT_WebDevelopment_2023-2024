import socket

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 1234
    BUFFER_SIZE = 2 ** 20

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        decoded = data.decode("UTF-8")
        print(decoded)
        s.sendto(b"Hello from server", sender_address)
