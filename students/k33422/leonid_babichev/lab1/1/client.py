import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

message = 'Hello, server'
client_socket.sendto(message.encode('utf-8'), server_address)

response, _ = client_socket.recvfrom(1024)
response_message = response.decode('utf-8')

print('Получен ответ от сервера:', response_message)

client_socket.close()
