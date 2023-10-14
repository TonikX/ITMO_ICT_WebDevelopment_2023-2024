import socket #модуль сокетов для работы с сетью
import threading #модуль  для создания потоков

def handle_client(conn, addr, user_number): #обработка клиентов
    while True:
        data = conn.recv(1024).decode() # принимаем сообщение от клиента и декодируем его
        if not data:
            break
        print(f"User-{user_number}: {data}") #вывод сообщения клиента
        broadcast_message(data, conn, user_number) #отправляет сообщение всем клиентам, кроме отправителя
    conn.close()  # закрываем соединение с клиентом
    remove_connection(conn) # удаление соединения клиента из списка активных соединений


def remove_connection(conn):
  connections.remove(conn)

def broadcast_message(message, from_conn, user_number): #отправляет сообщение всем клиентам, кроме отправителя
    for conn in connections:
        if conn != from_conn:
            conn.send(f"User-{user_number}: {message}".encode())

def server_program():
    server_socket = socket.socket() #создаем сокет сервера
    server_socket.bind((socket.gethostname(), 15000)) # связываем сервер с хостом и портом 15000
    server_socket.listen(5)  # до 5 соединений (до 5 клиентских соединений в очереди)
    print("Server started. Waiting for connections...")
    user_number = 1

    while True:
        conn, addr = server_socket.accept() #принимаем входящее соединение от клиента
        print("Connected to:", addr)
        connections.append(conn) #добавляем соединение в список активных соединений
        thread = threading.Thread(target=handle_client, args=(conn, addr, user_number))  #создаем новый поток для обработки клиента и передаем соединение и адрес клиента в handle
        thread.start()
        user_number += 1

    server_socket.close() #закрываем серверный сокет после завершения работы

if __name__ == '__main__':
    connections = []
    server_program()
