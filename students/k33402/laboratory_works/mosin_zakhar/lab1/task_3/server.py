import socket
import signal

port = 2448
buffsize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", port))
s.listen(1)
signal.signal(signal.SIGINT, signal.SIG_DFL)

def send_html_response(client_socket):
    with open("index.html", "rb") as html_file:
        html_content = html_file.read()
        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Content-Type: text/html\r\n"
        response += b"Content-Length: " + str(len(html_content)).encode() + b"\r\n"
        response += b"\r\n"
        response += html_content

        client_socket.send(response)

while True:
    try:
        print("Waiting for client to connect")
        client_socket, client_address = s.accept()
        print("Accepted connection from: ", client_address)
        request = client_socket.recv(buffsize)
        print(request.decode())

        send_html_response(client_socket)
        client_socket.close()

    except KeyboardInterrupt:
        print("Server terminated by user.")
        break