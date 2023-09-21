import threading
import socket

sock = socket.socket()

sock.bind((socket.gethostname(), 2347))
sock.listen(5)

clients = set()


def send_to_chat(current_client, msg):
    for client in clients:
        if client != current_client:
            client.send(msg.encode("utf-8"))


def listen(current_client):
    while True:
        try:
            msg = current_client.recv(10000).decode("utf-8")
            if msg == "q":
                send_to_chat(current_client, msg)
        except:
            clients.remove(current_client)
            break
        send_to_chat(current_client, msg)


while True:
    try:
        current_client, client_adress = sock.accept()
        clients.add(current_client)
        t = threading.Thread(target=listen, args=(current_client,))
        t.start()
    except KeyboardInterrupt:
        print("Server stoped")
        break

for client in clients:
    client.close()

sock.close()
