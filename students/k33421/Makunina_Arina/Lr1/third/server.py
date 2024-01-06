import socket

with open("index.html", "r") as file:
    content = file.read()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 7080))
server_socket.listen()

# Выводим ссылку для просмотра
print("Сервер запущен. Откройте браузер и перейдите по следующей ссылке:")
print("http://localhost:7080/")

while True:
    client_socket, _ = server_socket.accept()
    client_socket.recv(1024)
    response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n{content}"
    client_socket.send(response.encode())
    client_socket.close()
