import socket

serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024

TCPSocket = socket.create_connection(serverAdress)
 
try:
    data = input("Введите высоту и основание параллелограмма:")
    data = str.encode(data)
    TCPSocket.sendall(data)
    data = TCPSocket.recv(buffer)
    data = data.decode("utf-8")
    print("Площадь параллелограмма: {}".format(data))
 
finally:
    print("Closing socket")
    TCPSocket.close()