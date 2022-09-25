from socket import *

my_server = socket(AF_INET, SOCK_STREAM)
PORT = 1234
ADDRESS = ""
my_server.bind((ADDRESS, PORT))
my_server.listen()
client, client_address = my_server.accept()

while True:
    result = client.recv(1024)
    print(result.decode())
    client.send("Message received".encode())



