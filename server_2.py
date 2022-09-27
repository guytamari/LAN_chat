from socket import *
import threading

my_server = socket(AF_INET, SOCK_STREAM)
my_server.bind(("localhost", 4444))
my_server.listen()
client, clientaddr = my_server.accept()


def send(client):
    while True:
        msg_to_send = input("")
        client.sendall(msg_to_send.encode())
        if msg_to_send == "exit":
            my_server.close()


def receive(client):
    while True:
        msg_recv = client.recv(2048).decode()
        print("Client: " + msg_recv)
        if msg_recv == "exit":
            my_server.close()


t_send = threading.Thread(target=send, args=(client,))
t_recv = threading.Thread(target=receive, args=(client,))

t_send.start()
t_recv.start()
