import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 2222)
message = b"Hello, server" # наконец я нашёл применение к этому префексу
client_socket.sendto(message, server_address)

data, server_address = client_socket.recvfrom(1024) # Ждемc
print(f"Получено от сервера ({server_address}): {data.decode()}")


