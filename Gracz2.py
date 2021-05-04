from socket import *

HOST = '192.168.56.1'
PORT = 15200

BUFFER = 1024

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST,PORT))

name = input('Podaj nazwę gracza: ').encode()

client.send(name)

print(client.recv(BUFFER).decode())

print(client.recv(BUFFER).decode())