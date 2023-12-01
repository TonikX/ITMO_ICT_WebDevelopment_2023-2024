import socket

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:
        conn.bind(('127.0.0.1', 14900))
        while True:
            message_from, cl_address = conn.recvfrom(16384)
            decode_message = message_from.decode("utf-8")
            print('From client: ' + decode_message)
            message_to = 'Hello, client'.encode('utf-8')
            conn.sendto(message_to, cl_address)