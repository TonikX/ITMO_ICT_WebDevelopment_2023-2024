import socket
import threading

enc = "utf-8"
port = 2448

def receive_messages(client_socket):
    while True:
        try:
            incoming_message = client_socket.recv(1024).decode(enc)
            if not incoming_message:
                break
            else:
                print(f"-{incoming_message.strip()}")
        except Exception as e:
            print("Error while receiving message:", e)
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", port))

    username = input("Enter username: ")
    client_socket.send(username.encode(enc))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True  # thread dies when main thread (the only non-daemon thread) exits.
    receive_thread.start()

    while True:
        message = input("")
        client_socket.send(message.encode(enc))
        if message.lower() == "quit":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
