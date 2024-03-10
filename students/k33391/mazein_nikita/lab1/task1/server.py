import socket
import signal

# Create a UDP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1337))
signal.signal(signal.SIGINT, signal.SIG_DFL)

while True:
    # Set timeout
    s.settimeout(60)

    try:
        # Receive data from client
        data, addr = s.recvfrom(1024)
        print('Received data from client:', data.decode('utf-8'))

        # Send data to client
        data = bytes('Hello, client!', 'utf-8')
        s.sendto(data, addr)
        print('Sent data to client:', data.decode('utf-8'))

    except socket.timeout:
        print('No data received from client after 60 seconds')
        break

    except KeyboardInterrupt:
        print("Server terminated by user.")
        break

# Close socket
s.close()
