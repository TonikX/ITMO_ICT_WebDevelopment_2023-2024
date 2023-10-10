import socket
from time import sleep

IP = "127.0.0.1"

PORT = 14900
buffSize = 16384

listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = socket.gethostbyname(socket.gethostname())
#print(IP)

listener.bind((IP, PORT))

data = (listener.recvfrom(buffSize))
print(data[0].decode("utf-8"))
address = data[1]

ms = "Hello, Client"
listener.sendto(ms.encode('utf-8'), address)


#7 лаб по сетям
#Отчеты и защита
#дедлайны критические