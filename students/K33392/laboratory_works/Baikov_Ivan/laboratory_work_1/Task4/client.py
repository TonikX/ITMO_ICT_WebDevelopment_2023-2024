from socket import *
from threading import *

def message_handler(client):
    while True:
        msg = client.recv(1024).decode("utf-8")
        print(msg)


if __name__ == "__main__":
    ip= '127.0.0.1'
    port = 3003

    conn = socket(AF_INET, SOCK_STREAM)
    conn.connect((ip, port))

    receive_thread = Thread(target=message_handler, args=(conn,))
    receive_thread.start()

    while True:
        try:
            message = input()
            conn.send(message.encode("utf-8"))

        except KeyboardInterrupt:
            conn.close()
            print("Terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break
