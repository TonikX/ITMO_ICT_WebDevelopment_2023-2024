import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    
    try:
        client_socket.connect(server_address)
        
        # a - длина первого основания, b - длина второго основания, h - высота трапеции 
        a = float(input("Enter the length of the first parallel side: "))
        b = float(input("Enter the length of the second parallel side: "))
        h = float(input("Enter the height: "))
        
        # Отсылаем серверу
        data = f"{a},{b},{h}"
        client_socket.sendall(data.encode())
        
        # Получаем ответ от сервера
        result = client_socket.recv(1024).decode()
        print(f"The area of the trapezoid is: {result}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Закрываем канал
        client_socket.close()
        
if __name__ == "__main__":
    main()