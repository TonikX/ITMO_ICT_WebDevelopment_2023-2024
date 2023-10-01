import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    name = input ("Введите username до 20 знаков : ")
    if 1 < len(name) < 20:
        break

client.connect((socket.gethostname(), 1236))
print ("Вы подключились к серверу")
print ("Чтобы выйти, нажмите Q" )


def send_to_chat():
    while True:
        message = input("")
        print()
        if message == "Q":
            client.send(f"{name}: отключился".encode("utf-8"))
            break

        if message == "":
            continue

        client.send(f"{name}: {message}".encode("utf-8"))
        print(f"{name}: {message}")


def update_chat():
    while True:
        input_data = client.recv(1024)
        print(input_data.decode("utf-8"))


input_thread = threading.Thread(target=update_chat, name="input")
input_thread.start()

out_thread = threading.Thread(target=send_to_chat, name="out")
out_thread.start()

out_thread.join()

print("Сессия завершена")
client.close()
