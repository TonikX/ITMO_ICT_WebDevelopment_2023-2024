# import socket
# import threading
#
# IP = 'localhost'
# PORT = 5555
#
# def listen():
#     l_sock = socket.socket()
#     l_sock.bind((IP, PORT))
#     l_sock.listen()
import sys

# Move cursor to row 5, column 10
sys.stdout.write("\033[2J")

sys.stdout.write("\033[5;10H")
sys.stdout.write("\033[1m")
print("Hello World!")

# Move cursor to row 10, column 1
sys.stdout.write("\033[10;1H")

print("This is a new line.")
input()
sys.stdout.write("\033[0m")
sys.stdout.write("\033[0;0H")
sys.stdout.write("\033[2J")