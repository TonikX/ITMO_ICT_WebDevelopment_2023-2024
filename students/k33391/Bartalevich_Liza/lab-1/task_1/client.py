import socket


def send_and_receive_message():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 9090)

    try:
        client.sendto("Hello, server!".encode('utf-8'), server_address)
        resp, _ = client.recvfrom(1234)
        print("Response from server:", resp.decode("utf-8"))
    except Exception as e:
        print("Error:", str(e))
    finally:
        client.close()


if __name__ == "__main__":
    send_and_receive_message()