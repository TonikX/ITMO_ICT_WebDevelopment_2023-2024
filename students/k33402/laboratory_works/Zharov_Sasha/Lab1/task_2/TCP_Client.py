import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1234))
print("Введите высоту и длинну основания параллелограмма")
data = input("Пример: 2 7: ")
client.send(bytes(data, "utf-8"))

full_msg = ""

while True:
    msg = client.recv(1024)

    if len(msg) <= 0:
        break

    full_msg += msg.decode("utf-8")

print(full_msg)