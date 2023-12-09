import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 9999))
        response = client.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print('Error: ', str(e))
    finally:
        client.close()


if __name__ == '__main__':
    main()
