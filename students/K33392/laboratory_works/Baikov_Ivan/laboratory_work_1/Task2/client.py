from socket import *
if __name__ == "__main__":
    ip= '127.0.0.1'
    port = 3000

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((ip, port))

    input = input()

    client.sendall(input.encode())

    answer = client.recv(1024).decode()
    print(answer)