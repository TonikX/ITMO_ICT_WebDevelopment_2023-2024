import socket

HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384


def get_area_of_trapezoid(a, b, h):
    """
        >>> get_area_of_trapezoid(4, 7, 4)
        22.0
        >>> get_area_of_trapezoid(18, 6, 3.5)
        42.0
        >>> get_area_of_trapezoid(10, 58, 18)
        612.0
        >>> get_area_of_trapezoid(-4, 7, 4)
        'Such a trapezoid does not exist'
        >>> get_area_of_trapezoid(4, -7, 4)
        'Such a trapezoid does not exist'
        >>> get_area_of_trapezoid(0, 7, 4)
        'Such a trapezoid does not exist'
        >>> get_area_of_trapezoid(0, 0, 4)
        'Such a trapezoid does not exist'
        >>> get_area_of_trapezoid(4, 7, 0)
        'Such a trapezoid does not exist'
    """
    if a <= 0 or b < 0 or h <= 0 or (a == b == 0):
        return "Such a trapezoid does not exist"

    return (a + b) * h / 2


if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:  # TCP
        conn.bind(server_address)
        conn.listen(10)
        print('Server is waiting...')

        timeout = 30
        while True:
            conn.settimeout(timeout)
            try:
                client_socket, address = conn.accept()
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(timeout))
                break

            with client_socket:
                message = "To find the area of a trapezoid, enter the bases a, b and the height h separated by a space\n(decimal separator dot)"
                client_socket.sendall(message.encode('utf-8'))

                recieved = client_socket.recv(BUFF_SIZE).decode('utf-8')
                print(f'Client: {recieved}')

                try:
                    a, b, h = map(float, recieved.split())
                    result = str(get_area_of_trapezoid(a, b, h))
                    client_socket.sendall(result.encode('utf-8'))
                except Exception:
                    client_socket.sendall("Something went wrong :(\nPlease double check your data".encode('utf-8'))
