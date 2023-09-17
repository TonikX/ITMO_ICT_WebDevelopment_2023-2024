import socket

HOST = "127.0.0.1"
PORT = 3000
DATA_RECV = 2048
SERVER_MESSAGE = b"Hello, server"


def main():
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_conn.connect((HOST, PORT))

    try:
        while True:
            message = input("Send message?(y/n)")

            match message:
                case "y":
                    socket_conn.send(SERVER_MESSAGE)

                    reply_message = socket_conn.recv(DATA_RECV).decode("utf-8")
                    print(f"Server reply: {reply_message}")
                case "n":
                    break
                case _:
                    continue
    except KeyboardInterrupt:
        pass
    finally:
        socket_conn.close()

    print(f"Connection closed, bye")


if __name__ == "__main__":
    main()
