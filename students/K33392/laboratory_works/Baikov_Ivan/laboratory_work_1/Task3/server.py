from socket import *
content = open("Task3/index.html").read()

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 3000

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen()

    while True:
        try:
            print("Waiting for a connection...")
            client, addr = server.accept()
            print(f"Accepted connection from {addr}")

            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content

            client.send(response.encode())

            client.close()

        except KeyboardInterrupt:
            print("Server terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

    server.close()
