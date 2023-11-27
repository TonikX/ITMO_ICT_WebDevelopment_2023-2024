from socket import *
from calculate import calculate

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

            while True:
                data = client.recv(1024).decode("utf-8")

                if not data:
                    print(f"Client {addr} disconnected.")
                    break

                operation, a, b = data.split(',')
                a, b = float(a), float(b)

                if operation == "hyp":
                    result = calculate(cath1=a, cath2=b)
                elif operation == "cath":
                    result = calculate(cath1=a, hyp=b)
                else:
                    result = "Invalid operation"

                client.send(bytes(str(result), encoding="utf-8"))

        except KeyboardInterrupt:
            print("Server terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

    server.close()
