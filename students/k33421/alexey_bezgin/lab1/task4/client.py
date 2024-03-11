import socket
import threading

# Функция обработки входящих сообщений от сервера
def receive_message_handler(client):
    while True:
        # Получаем сообщение от сервера и декодируем его из байтовой строки
        message_obj = client.recv(16384).decode("utf-8")
        # Выводим полученное сообщение на экран
        print(message_obj)

if __name__ == "__main__":
    # Задаем IP-адрес и порт сервера, к которому будем подключаться.
    server_ip = "127.0.0.1"
    server_port = 7011

    # Создаем TCP сокет (SOCK_STREAM) и устанавливаем соединение с сервером.
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_ip, server_port))

    # Создаем отдельный поток для приема сообщений от сервера
    receive_thread = threading.Thread(target=receive_message_handler, args=(conn,))
    receive_thread.start()

    while True:
        try:
            # Читаем сообщение с клавиатуры
            message = input()
            # Отправляем сообщение серверу, предварительно кодируя его в байты
            conn.send(message.encode("utf-8"))
        except KeyboardInterrupt:
            # Закрываем соединение при нажатии Ctrl+C и завершаем программу
            conn.close()
            break

