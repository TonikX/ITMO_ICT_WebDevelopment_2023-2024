if __name__ == '__main__':
    import json
    import socket

    a = int(input("Enter first base of the trapezoid: "))
    b = int(input("Enter second base of the trapezoid: "))
    h = int(input("Enter height of the trapezoid: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9090))
    sock.send(json.dumps({"a": a, "b": b, "h": h}).encode("utf-8"))

    data = sock.recv(1024)
    print("Аrea of a trapezoid is " + data.decode("utf-8"))

    sock.close()
