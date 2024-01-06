import socket

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        
        while True:
            data, addr = conn.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            conn.sendto(b"Hello, client!", addr)
