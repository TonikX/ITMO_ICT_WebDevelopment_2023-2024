import socket
import json

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048


def main():
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conn.connect((HOST, PORT))

    while True:
        try:
            message = input(
                "Calculate trapezoid area\nPlease enter a, b and h separated by spaces:\n"
            )
            try:
                a, b, h = list(map(float, message.split(" ")))
            except:
                print("Got wrong arguments, try again!")
                continue

            socket_conn.send(bytes(json.dumps({"a": a, "b": b, "h": h}), "utf-8"))

            raw_response = socket_conn.recv(RECV_SIZE).decode()
            if not raw_response:
                break

            response = json.loads(raw_response)
            if "error" in response:
                print(f"Got error from server: {response['error']}")
                continue

            print(f'Got answer from server: {response["data"]}')
            break
        except Exception:
            continue
        except KeyboardInterrupt:
            break

    socket_conn.close()
    print(f"Connection closed, bye")


if __name__ == "__main__":
    main()
