import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', 2002))

print("Please enter the coefficients before the terms of the quadratic polynomial in descending order of its degrees:")

try:
    while True:
        a,b,c = map(float,input().split())
        arr = [a,b,c]
        arr = map(str,arr)
        message = ' '.join(arr)
        client.send(bytes(message, "UTF-8"))
        data = client.recv(4096)
        print(data.decode("UTF-8"))
except:
    print("incorrect input")
client.close()