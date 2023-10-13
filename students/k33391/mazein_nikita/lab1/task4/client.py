import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            incoming_message = client_socket.recv(1024).decode('utf-8')
            if not incoming_message:
                break
            else:
                print(f"-{incoming_message.strip()}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1337))

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True  # thread dies when main thread (the only non-daemon thread) exits.
    receive_thread.start()

    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == "exit":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
