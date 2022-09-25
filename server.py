from socket import *

my_server = socket(AF_INET, SOCK_STREAM)
PORT = 1234
ADDRESS = "localhost"
my_server.bind((ADDRESS, PORT))
my_server.listen()
client, client_address = my_server.accept()

while True:
    result = client.recv(1024).decode()
    print(result)
    client.send(input("Message: ").encode('utf-8'))



