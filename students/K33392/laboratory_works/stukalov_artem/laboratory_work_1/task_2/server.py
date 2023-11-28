import socket
from loguru import logger
import json

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048
MAX_PENDING_CONNECTIONS = 10
ERROR_MESSAGE = bytes(
    json.dumps({"error": "One of the parameters was missing or less or equal to zero"}),
    "utf-8",
)


def get_trapezoid_area(a, b, h):
    return (a + b) * h / 2


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

            def close_client():
                client.close()
                logger.info(f"Close client connection")

            while True:
                try:
                    message = client.recv(RECV_SIZE).decode()
                    if message == "":
                        break

                    message = json.loads(message)
                    logger.info(f"Got clinet({address}) message: {message}")

                    if (
                        message.get("a", 0) <= 0
                        or message.get("b", 0) <= 0
                        or message.get("h", 0) <= 0
                    ):
                        client.send(ERROR_MESSAGE)
                        continue

                    client.send(
                        bytes(
                            json.dumps({"data": get_trapezoid_area(**message)}), "utf-8"
                        )
                    )
                    break
                except Exception:
                    logger.info("Failed to recv client message")
                    close_client()
                    break
                except KeyboardInterrupt as error:
                    close_client()
                    raise error
        except:
            socket_conn.close()
            logger.info(f"Server was stopped")
            break


if __name__ == "__main__":
    main()
