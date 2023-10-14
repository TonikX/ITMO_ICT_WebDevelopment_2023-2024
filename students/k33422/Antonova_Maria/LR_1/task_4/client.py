import socket
import threading


def receive_messages(client_socket):
  while True:
    data = client_socket.recv(1024).decode()
    if not data:
      break
    print(f"Server-{client_socket.getsockname()[1]}: {data}")


def client_program():
  host = socket.gethostname()
  port = 15000
  client_socket = socket.socket()
  client_socket.connect((host, port))
  print("Connected to the server.")

  receive_thread = threading.Thread(target=receive_messages,
                                    args=(client_socket, ))
  receive_thread.start()

  while True:
    message = input(" -> ")
    client_socket.send(message.encode())
    if message.lower().strip() == 'bye':
      break

  client_socket.close()


if __name__ == '__main__':
  client_program()
