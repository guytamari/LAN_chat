import threading
from socket import *

try:
    my_client = socket(AF_INET, SOCK_STREAM)
    host = "localhost"
    port = 1234
    my_client.connect((host, port))
except ConnectionRefusedError and OSError:
    print("Could not connect to server...")


def thread_sending():
    while True:
        message_to_send = input()
        my_client.send(message_to_send.encode())


def thread_receiving():
    while True:
        message = my_client.recv(1024).decode()
        print(message)


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
