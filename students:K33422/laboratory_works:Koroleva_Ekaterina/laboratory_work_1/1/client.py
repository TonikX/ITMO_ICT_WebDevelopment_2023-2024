from socket import *

message = "Hello, server!"
encoded_message = str.encode(message)

HOST = ('localhost', 10000)
client = socket(AF_INET, SOCK_DGRAM)

client.sendto(encoded_message, HOST)
server_message = client.recvfrom(1024)
message_info = server_message[0].decode()
print(message_info)