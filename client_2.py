from socket import *
import threading

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 4444))


def send(client):
    while True:
        msg_to_send = input("")
        client.sendall(msg_to_send.encode())
        if msg_to_send == "exit":
            client.close()


def receive(client):
    while True:
        msg_recv = client.recv(2048).decode()
        print("Server: " + msg_recv)
        if msg_recv == "exit":
            client.close()


t_send = threading.Thread(target=send, args=(client,))
t_recv = threading.Thread(target=receive, args=(client,))
t_send.start()
t_recv.start()
