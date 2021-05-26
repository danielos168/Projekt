from socket import *
from threading import Thread
from Game_Characters import *
from random import randrange

HOST = 'localhost'
PORT = 2223
BUFFER = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(3)


def handle_answers1(client_socket1, x, ans, t):
    if ans in Character_List_Keys:
        answer = Character_List[x][ans]
        answer = str(answer).encode()
        client_socket1.send(answer)
    else:
        ans = int(ans)
        if Character_List[ans]['postac'] == Character_List[x]['postac']:
            answer = 'True'.encode()
            client_socket1.send(answer)
        else:
            answer = 'False'.encode()
            client_socket1.send(answer)


def handle_answers2(client_socket2, t, ans2, x):
    if ans2 in Character_List_Keys:
        answer = Character_List[t][ans2]
        answer = str(answer).encode()
        client_socket2.send(answer)
    else:
        ans2 = int(ans2)
        if Character_List[ans2]['postac'] == Character_List[t]['postac']:
            answer = 'True'.encode()
            client_socket2.send(answer)
        else:
            answer = 'False'.encode()
            client_socket2.send(answer)


def handle_connection(client_socket1, address1, client_socket2, address2):
    while True:
        print(f"Uzyskano połaczenie od {address1}")
        gracz1 = client_socket1.recv(BUFFER).decode()
        print(gracz1)
        t = randrange(0, len(Character_List))
        msg1 = f"Witaj na serwerze, {gracz1}. Twoja postać to {Character_List[t]['postac']} z bajki {Character_List[t]['tytuł']}".encode()

        client_socket1.send(msg1)

        print(f"Uzyskano połaczenie od {address2}")
        gracz2 = client_socket2.recv(BUFFER).decode()
        print(gracz2)
        x = randrange(0, len(Character_List))
        msg2 = f"Witaj na serwerze, {gracz2}. Twoja postać to {Character_List[x]['postac']} z bajki {Character_List[x]['tytuł']}".encode()

        client_socket2.send(msg2)
        while True:
            if client_socket1.recv:
                ans = client_socket1.recv(BUFFER).decode()
                handle_answers1(client_socket1, x, ans, t)
            if client_socket2.recv:
                ans2 = client_socket2.recv(BUFFER).decode()
                handle_answers2(client_socket2, t, ans2, x)


while True:
    client_sock1, addr1 = server.accept()
    print(f"Accepted connection from {addr1}...Waiting for second player")
    client_sock2, addr2 = server.accept()
    print(f"Accepted connection from {addr2}...Waiting for second player")
    t = Thread(target=handle_connection, args=(client_sock1, addr1, client_sock2, addr2))
    t.start()
