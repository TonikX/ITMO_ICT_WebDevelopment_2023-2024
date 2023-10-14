import socket
import math


def solve_quadratic(a, b, c):
  D = b**2 - 4 * a * c
  if D < 0:
    return "no sols. D<0"
  else:
    sol1 = (-b - math.sqrt(D)) / (2 * a)
    sol2 = (-b + math.sqrt(D)) / (2 * a)
    return sol1, sol2


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind(('localhost', 12345))
  server_socket.listen(1)

  while True:
    client_socket, addr = server_socket.accept()
    with client_socket:
      print(f"new request: {addr}")
      data = client_socket.recv(1024).decode('utf-8')
      a, b, c = map(float, data.split())
      result = solve_quadratic(a, b, c)
      client_socket.send(str(result).encode('utf-8'))