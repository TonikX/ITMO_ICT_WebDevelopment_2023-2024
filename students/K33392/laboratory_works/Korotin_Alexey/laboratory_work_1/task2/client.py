import socket
from json import dumps

if __name__ == "__main__":
    DEST = ("localhost",  1234)
    BUFFER_SIZE = 2 ** 20
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(DEST)
        params = {
            "a": "1",
            "b": "2",
            "c": "3"
        }
        json_string = dumps(params, indent=4)
        s.send(json_string.encode("UTF-8"))

        data = s.recv(BUFFER_SIZE)

        print(data.decode("UTF-8"))
