import socket

def calculate_trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening for connections...")
    
    try:
        while True:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            
            try:
                # Receive data from the client
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                
                # Parse received data (assuming it's in the format "a,b,h")
                a, b, h = map(float, data.split(','))
                
                # Calculate the trapezoid area
                result = calculate_trapezoid_area(a, b, h)
                
                # Send the result back to the client
                client_socket.sendall(str(result).encode())
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                # Close the client socket
                client_socket.close()
    except KeyboardInterrupt:
        print("Server terminated by user.")
    finally:
        # Close the server socket when done
        server_socket.close()

if __name__ == "__main__":
    main()
