import socket

serverAdress   = ("127.0.0.1", 9090)
buffer         = 8192

# Подключаемся к серверу, получаем сокет
TCPSocket = socket.create_connection(serverAdress)
print("=== connected to the server ===\n")
 
try:
    # Получем данные от сервера
    data = TCPSocket.recv(buffer)
    data = data.decode("utf-8")
    print(data)
 
finally:
    print("\n=== Closing socket ===")
    TCPSocket.close()