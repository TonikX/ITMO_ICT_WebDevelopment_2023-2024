import socket

port = 2002
data_recv = 2048
host = "127.0.0.1"

print("Parallelogram area calculation")

def main():
    while True:
        #input the height and the base of Parallelogram
        h_str = input("Enter height: ")
        b_str = input("Enter base: ")
        #check if the input are positive integer
        try:
            h = int(h_str)
            b = int(b_str)
            if h > 0 and b > 0:
                break
            else:
                print("Height and/or base is not positive integers.")
        except ValueError:
            print("Invalid input. Please enter valid integer values for height and base.")

    msg = (h_str+" "+b_str).encode("utf-8")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    try:
        #Send input to server
        s.send(msg)
        #Get the answer from server
        msg, address = s.recvfrom(data_recv)
        print("Area of parallelogram is: ", msg.decode("utf-8"))
        
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()