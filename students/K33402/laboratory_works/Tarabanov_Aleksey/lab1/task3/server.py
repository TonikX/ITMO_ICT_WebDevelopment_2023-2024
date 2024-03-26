import socket


HOST = '127.0.0.1'
PORT = 22222
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"ссылка -> http://{HOST}:{PORT}/")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"подключение от {client_address}")
    with open("index.html", 'r') as file:
        html_content = file.read()
    # Тут кстати советовалось использовать \r, что бы переносить на начало строки. но я так посмотрел, и не нашёл причин для этого.
    http_response = f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(html_content)}\n\n{html_content}"
    #print(http_response)
    client_socket.sendall(http_response.encode('utf-8'))
