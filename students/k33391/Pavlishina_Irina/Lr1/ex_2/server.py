import socket
import threading

"""
    TCP Server code.

     Can recieve data, calculate smth and send result back to client, creating different thread for each client.  
"""


def quadratic_equation(a, b, c):
    """
    Function calculating the quadratic equation.

    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant
    :return: answers
    """

    x1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)
    return x1, x2


def parce_string(string):
    """
    Function for parsing client message

    :param string: client message
    :return: split string

    """

    return string.split()


def chat(client):
    """
    Function for runnning connection with a client.

    :param client:  [<client_socket>, <client_address>]
    :return: Nothing
    """

    while True:
        client_socket = client[0]
        client_address = client[1]

        data = client_socket.recv(65536).decode('utf-8')
        a, b, c = parce_string(data)
        x1, x2 = quadratic_equation(int(a), int(b), int(c))
        ans = f"X1= {x1}, X2= {x2}"
        client_socket.sendto(ans.encode(), client_address)


def main():
    """
    Main function running server.
    Bind lockalhost and listen it. Creating new thread every time new client connect it.

    :return: Nothing
    """
    PORT = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(10)

    while True:

        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=([client_socket, client_address], ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break


if __name__ == "__main__":
    main()