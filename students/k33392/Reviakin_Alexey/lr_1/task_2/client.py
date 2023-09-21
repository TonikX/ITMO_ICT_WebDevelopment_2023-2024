import socket

print("Введите стороны треугольника через запятую без пробела (Пример: 3,4):")
values = input()

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((socket.gethostname(), 1236))
conn.send(values.encode())
data = conn.recv(1024).decode("utf-8")
print(data)
conn.close()
