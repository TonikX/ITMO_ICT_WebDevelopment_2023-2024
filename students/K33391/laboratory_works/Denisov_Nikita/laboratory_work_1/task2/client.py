# Вариант: поиск площади параллелограмма
import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
  
    a = float(input("Введите сторону a: "))
    h = float(input("Введите высоту h: "))

    message = f"{a},{h}"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Ответ от сервера: {response}")

except Exception as e:
    print(f"Ошибка при обмене данными с сервером: {e}")

finally:
    client_socket.close()
