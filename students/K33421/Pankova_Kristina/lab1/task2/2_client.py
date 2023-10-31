
import socket

HOST = '127.0.0.1'
PORT = 5000

def get_input():
    a = input('Enter the first cathetus (or leave blank): ')
    b = input('Enter the second cathetus (or leave blank): ')
    c = input('Enter the hypotenuse (or leave blank): ')
    return f'{a},{b},{c}'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = get_input()
        s.sendall(data.encode())
        result = s.recv(1024).decode()
        print(f'Result: {result}')