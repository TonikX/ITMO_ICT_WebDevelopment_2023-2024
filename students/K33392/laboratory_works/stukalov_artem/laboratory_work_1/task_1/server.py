import socket
from loguru import logger

HOST = "127.0.0.1"
PORT = 3000
DATA_RECV = 2048
REPLY_MESSAGE = b"Hello, client"


def main():
    logger.info("Starting server...")
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_conn.bind((HOST, PORT))
    logger.info(f"Server started on {HOST}:{PORT}")

    try:
        while True:
            (raw_message, client_address) = socket_conn.recvfrom(DATA_RECV)
            message = raw_message.decode("utf-8")
            logger.info(f"Message from clinet {client_address[1]}: {message}")

            socket_conn.sendto(REPLY_MESSAGE, client_address)
    except KeyboardInterrupt:
        pass
    finally:
        socket_conn.close()
        logger.info(f"Server stopped")


if __name__ == "__main__":
    main()
