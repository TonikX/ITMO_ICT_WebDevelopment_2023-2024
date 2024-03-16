import socket
import signal

enc = "utf-8"
port = 2448
buffsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", port))
signal.signal(signal.SIGINT, signal.SIG_DFL)

while True:
    s.settimeout(60)

    try:
        data, addr = s.recvfrom(buffsize)
        print("Received data from client:", data.decode(enc))

        data = bytes("Hello, client", enc)
        s.sendto(data, addr)
        print("Sent data to client:", data.decode(enc))

    except socket.timeout:
        print("No data has been received from client within 60 seconds ._.")
        break

    except KeyboardInterrupt:
        print("Server terminated by user :(")
        break

s.close()
