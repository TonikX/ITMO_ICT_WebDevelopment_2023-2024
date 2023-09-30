# Вариант: поиск площади параллелограмма
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)


server_socket.listen(1)
print("Сервер ожидает подключения клиента...")

while True:
  
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент с адресом: {client_address}")

    try:
        
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение от клиента: {data}")

        a, h = map(float, data.split(','))

        result = a * h

        response_message = f"Площадь параллелограмма: {result}"
        client_socket.send(response_message.encode('utf-8'))

    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")

    finally:
        client_socket.close()


