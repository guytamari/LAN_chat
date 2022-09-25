import threading
from socket import *
done = False
try:
    my_client = socket(AF_INET, SOCK_STREAM)
    host = "localhost"
    port = 1234
    my_client.connect((host, port))
except ConnectionRefusedError or OSError or ConnectionRefusedError:
    print("Could not connect to server...")
else:
    while not done:
        my_client.send(input("Message: ").encode('utf-8'))
        msg = my_client.recv(1024).decode('utf-8')
        if msg == 'quit':
            done = True
        else:
            print(msg)


