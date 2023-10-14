import socket

while True:
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(('localhost', 12345))

  print("(a, b, c):")
  a, b, c = map(float, input().split())
  client_socket.send(f"{a} {b} {c}".encode('utf-8'))

  result = client_socket.recv(1024).decode('utf-8')
  print(f"Result: {result}")

  client_socket.close()