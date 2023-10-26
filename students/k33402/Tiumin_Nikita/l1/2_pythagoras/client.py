import socket
import pickle


def run():
    input_in_progress = True

    while input_in_progress:
        a = input("enter a ==>")
        b = input("enter b ==>")

        if a.isnumeric() and b.isnumeric():
            input_in_progress = False
        else:
            print('a, b must be numbers, please re-enter the values')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9090))

    payload = {a, b}

    sock.send(pickle.dumps(payload))

    res = sock.recv(1024)
    sock.close()

    print(res.decode('utf-8'))


if __name__ == '__main__':
    run()
