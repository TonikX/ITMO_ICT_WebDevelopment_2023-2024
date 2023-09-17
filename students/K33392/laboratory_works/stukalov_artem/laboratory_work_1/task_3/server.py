import socket
from loguru import logger
import pathlib

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048
MAX_PENDING_CONNECTIONS = 10
RESPONSE_TYPE = "HTTP/1.0 200 OK"
HEADERS = "\n".join(["Content-Type: text/html"]) + "\n"
CURRENT_DIR = pathlib.Path(__file__).parent.resolve()


def main():
    logger.info("Starting server...")
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conn.bind((HOST, PORT))
    socket_conn.listen(MAX_PENDING_CONNECTIONS)
    logger.info(f"Server started on {HOST}:{PORT}")

    while True:
        try:
            (client, address) = socket_conn.accept()
            logger.info(f"Got clinet connection {address}")

            client.recv(RECV_SIZE)

            with open(CURRENT_DIR.joinpath("./index.html"), "r") as file:
                response = "\n".join([RESPONSE_TYPE, HEADERS, file.read()])
                print(response)
                client.send(response.encode("utf-8"))

            client.close()
            logger.info(f"Close clinet connection {address}")

        except KeyboardInterrupt:
            socket_conn.close()
            logger.info(f"Server was stopped")
            break


if __name__ == "__main__":
    main()
