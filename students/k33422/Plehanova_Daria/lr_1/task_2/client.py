import socket

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect(('127.0.0.1', 8888))
        
        data = conn.recv(1024)
        print(data.decode())
        
        data = input()
        conn.sendall(data.encode())
        
        data = conn.recv(1024)
        print(data.decode())
