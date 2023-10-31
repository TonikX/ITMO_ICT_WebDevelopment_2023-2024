from socket import *

message = "Hello, server!"
encoded_message = str.encode(message)

HOST = (gethostname(), 10000)
client = socket(AF_INET, SOCK_STREAM)
client.connect(HOST)
server_message = client.recv(1024).decode()

print(server_message)
user_input = int(input())

if user_input == 1:
    print("Введите значения катетов через запятую")
else:
    print("Введите значения гипотенузы и катета через запятую")

input_data = input()
print(str(user_input) + input_data)
client.sendall((str(user_input) + input_data).encode())

answer = client.recv(1024).decode()
print(answer)


