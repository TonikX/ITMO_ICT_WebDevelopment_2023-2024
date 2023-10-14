import socket
import threading


def handle_client(conn, addr):
  while True:
    data = conn.recv(1024).decode()
    if not data:
      break
    print(f"User-{addr[1]}: {data}")
    broadcast_message(data, conn)
  conn.close()
  remove_connection(conn)


def broadcast_message(message, from_conn):
  for conn in connections:
    if conn != from_conn:
      conn.send(message.encode())


def remove_connection(conn):
  connections.remove(conn)


def server_program():
  server_socket = socket.socket()
  server_socket.bind((socket.gethostname(), 15000))
  server_socket.listen(5)  # Allow up to 5 connections in the queue
  print("Server started. Waiting for connections...")

  while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    connections.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

  server_socket.close()


if __name__ == '__main__':
  connections = []
  server_program()
