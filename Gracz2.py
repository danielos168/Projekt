from socket import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from time import sleep

HOST = 'localhost'
PORT = 2223

BUFFER = 1024

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

name = input('Podaj nazwę gracza: ').encode()

client.send(name)

# Okno pierwsze - zdjęcia postaci
root = Tk()
root.title('Guess who!?')
root.iconbitmap('Photos/zapytanie.ico')
root.geometry("577x560")
root['background'] = '#856ff8'


def changeState(button_name):
    if (button_name['relief'] == "solid"):
        button_name['relief'] = "sunken"
    else:
        button_name['relief'] = "solid"


img_1 = PhotoImage(file="Photos/Character_1.png")
img_2 = PhotoImage(file="Photos/Character_2.png")
img_3 = PhotoImage(file="Photos/Character_3.png")
img_4 = PhotoImage(file="Photos/Character_4.png")
img_5 = PhotoImage(file="Photos/Character_5.png")
img_6 = PhotoImage(file="Photos/Character_6.png")

img_7 = PhotoImage(file="Photos/Character_7.png")
img_8 = PhotoImage(file="Photos/Character_8.png")
img_9 = PhotoImage(file="Photos/Character_9.png")
img_10 = PhotoImage(file="Photos/Character_10.png")
img_11 = PhotoImage(file="Photos/Character_11.png")
img_12 = PhotoImage(file="Photos/Character_12.png")

img_13 = PhotoImage(file="Photos/Character_13.png")
img_14 = PhotoImage(file="Photos/Character_14.png")
img_15 = PhotoImage(file="Photos/Character_15.png")
img_16 = PhotoImage(file="Photos/Character_16.png")
img_17 = PhotoImage(file="Photos/Character_17.png")
img_18 = PhotoImage(file="Photos/Character_18.png")

img_19 = PhotoImage(file="Photos/Character_19.png")
img_20 = PhotoImage(file="Photos/Character_20.png")
img_21 = PhotoImage(file="Photos/Character_21.png")
img_22 = PhotoImage(file="Photos/Character_22.png")
img_23 = PhotoImage(file="Photos/Character_23.png")
img_24 = PhotoImage(file="Photos/Character_24.png")

Button_1 = Button(root, image=img_1, borderwidth=4, relief="solid", command=lambda: changeState(Button_1))
Button_2 = Button(root, image=img_2, borderwidth=4, relief="solid", command=lambda: changeState(Button_2))
Button_3 = Button(root, image=img_3, borderwidth=4, relief="solid", command=lambda: changeState(Button_3))
Button_4 = Button(root, image=img_4, borderwidth=4, relief="solid", command=lambda: changeState(Button_4))
Button_5 = Button(root, image=img_5, borderwidth=4, relief="solid", command=lambda: changeState(Button_5))

Button_6 = Button(root, image=img_6, borderwidth=4, relief="solid", command=lambda: changeState(Button_6))
Button_7 = Button(root, image=img_7, borderwidth=4, relief="solid", command=lambda: changeState(Button_7))
Button_8 = Button(root, image=img_8, borderwidth=4, relief="solid", command=lambda: changeState(Button_8))
Button_9 = Button(root, image=img_9, borderwidth=4, relief="solid", command=lambda: changeState(Button_9))
Button_10 = Button(root, image=img_10, borderwidth=4, relief="solid", command=lambda: changeState(Button_10))

Button_11 = Button(root, image=img_11, borderwidth=4, relief="solid", command=lambda: changeState(Button_11))
Button_12 = Button(root, image=img_12, borderwidth=4, relief="solid", command=lambda: changeState(Button_12))
Button_13 = Button(root, image=img_13, borderwidth=4, relief="solid", command=lambda: changeState(Button_13))
Button_14 = Button(root, image=img_14, borderwidth=4, relief="solid", command=lambda: changeState(Button_14))
Button_15 = Button(root, image=img_15, borderwidth=4, relief="solid", command=lambda: changeState(Button_15))

Button_16 = Button(root, image=img_16, borderwidth=4, relief="solid", command=lambda: changeState(Button_16))
Button_17 = Button(root, image=img_17, borderwidth=4, relief="solid", command=lambda: changeState(Button_17))
Button_18 = Button(root, image=img_18, borderwidth=4, relief="solid", command=lambda: changeState(Button_18))
Button_19 = Button(root, image=img_19, borderwidth=4, relief="solid", command=lambda: changeState(Button_19))
Button_20 = Button(root, image=img_20, borderwidth=4, relief="solid", command=lambda: changeState(Button_20))

Button_21 = Button(root, image=img_21, borderwidth=4, relief="solid", command=lambda: changeState(Button_21))
Button_22 = Button(root, image=img_22, borderwidth=4, relief="solid", command=lambda: changeState(Button_22))
Button_23 = Button(root, image=img_23, borderwidth=4, relief="solid", command=lambda: changeState(Button_23))
Button_24 = Button(root, image=img_24, borderwidth=4, relief="solid", command=lambda: changeState(Button_24))

Button_1.grid(row=0, column=0)
Button_2.grid(row=0, column=1)
Button_3.grid(row=0, column=2)
Button_4.grid(row=0, column=3)
Button_5.grid(row=0, column=4)
Button_6.grid(row=0, column=5)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)
Button_10.grid(row=1, column=3)
Button_11.grid(row=1, column=4)
Button_12.grid(row=1, column=5)

Button_13.grid(row=2, column=0)
Button_14.grid(row=2, column=1)
Button_15.grid(row=2, column=2)
Button_16.grid(row=2, column=3)
Button_17.grid(row=2, column=4)
Button_18.grid(row=2, column=5)

Button_19.grid(row=3, column=0)
Button_20.grid(row=3, column=1)
Button_21.grid(row=3, column=2)
Button_22.grid(row=3, column=3)
Button_23.grid(row=3, column=4)
Button_24.grid(row=3, column=5)

# Okno drugie - zapytania, odpowiedzi i wynik
root2 = Tk()
root2.title('Guess who!?')
root2.iconbitmap('Photos/zapytanie.ico')
root2.geometry("450x520")
root2['background'] = '#856ff8'
t = client.recv(BUFFER).decode()


class Punkt:
    def __init__(self):
        self._i = 8

    def get(self):
        return self._i

    def set(self, value):
        self._i = value


Punkty = Punkt()
txt = t + "."
text = Label(root2, text=txt, bg='#856ff8')
txt2 = f"Ilość punktów początkowych: {Punkty.get()}"
text2 = Label(root2, text=txt2, bg='#856ff8')
text.pack()
text2.pack()


# Funkcja na koniec gry.
def Koniec():
    answer = Label(root2, text=f'Twoja liczba punktów wynosi {Punkty.get()}, nie możesz zadać więcej pytań.',
                   bg='#FF0000')
    answer.pack()


# Buttony  pytaniami i fukcje do odpowiedzi
def response1(Punkty):
    Punkty.set(Punkty.get() - 1)
    t = 'Czy_człowiek'.encode()
    if Punkty.get() == -1:
        Koniec()
    else:
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f' Postać przeciwnika jest człowiekiem. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie jest człowiekiem. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton1 = Button(root2, text="Czy twoja postać jest człowiekiem?", fg="black", bg="grey", width=200,
                   command=lambda: response1(Punkty))


def response2(Punkty):
    Punkty.set(Punkty.get() - 1)
    t = 'Czy_kobieta'.encode()
    if Punkty.get() == -1:
        Koniec()
    else:
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika jest kobietą. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie jest kobietą. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton2 = Button(root2, text="Czy twoja postać jest kobietą?", fg="black", bg="grey", width=200,
                   command=lambda: response2(Punkty))


def response3(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_broda'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika ma brodę. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie ma brody. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton3 = Button(root2, text="Czy twoja postać ma brodę?", fg="black", bg="grey", width=200,
                   command=lambda: response3(Punkty))


def response4(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_nakrycie_głowy'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika ma nakrycie głowy. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie ma nakrycia głowy. Punkty: {Punkty.get()}',
                           bg='#856ff8')
        answer.pack()


myButton4 = Button(root2, text="Czy twoja postać ma nakrycie głowy?", fg="black", bg="grey", width=200,
                   command=lambda: response4(Punkty))


def response5(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_złoczyńca'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika jest złoczyńcą. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie jest złoczyńcą. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton5 = Button(root2, text="Czy twoja postać jest złoczyńcą?", fg="black", bg="grey", width=200,
                   command=lambda: response5(Punkty))


def response6(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_okulary'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika ma okulary. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie ma okularów. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton6 = Button(root2, text="Czy twoja postać ma okulary?", fg="black", bg="grey", width=200,
                   command=lambda: response6(Punkty))


def response7(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_gruby'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika jest przy tuszy. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie jest przy tuszy. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton7 = Button(root2, text="Czy twoja postać jest przy tuszy?", fg="black", bg="grey", width=200,
                   command=lambda: response7(Punkty))


def response8(Punkty):
    Punkty.set(Punkty.get() - 1)
    if Punkty.get() == -1:
        Koniec()
    else:
        t = 'Czy_łysy'.encode()
        client.send(t)
        x = client.recv(BUFFER).decode()
        if x == 'True':
            answer = Label(root2, text=f'Postać przeciwnika jest łysy. Punkty: {Punkty.get()}', bg='#856ff8')
        else:
            answer = Label(root2, text=f'Postać przeciwnika nie jest łysy. Punkty: {Punkty.get()}', bg='#856ff8')
        answer.pack()


myButton8 = Button(root2, text="Czy twoja postać jest łysa?", fg="black", bg="grey", width=200,
                   command=lambda: response8(Punkty))

items = ("Aladyn", "Dżasmina", "Dżin", "Dżafar", "Kapitan Hak", "Piotruś Pan", "Wendy", "Herkules", "Hades", "Elastyna",
         "Pan Iniemamocny", "Elsa", "Olaf", "Ariel", "Baloo", "Bestia", "Lumiere", "Geppetto", "Roszpunka",
         "Szeryf Chudy",
         "Pan Bulwa", "Kuzco", "Mushu", "Clayton")
combobox = Combobox(root2)
combobox['values'] = items
combobox.current(0)


def check():
    t = str(combobox.current()).encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text=f'Udało Ci się zakończyć grę! Zdobyte punkty: {Punkty.get()}', bg='#856ff8')
    else:
        answer = Label(root2, text=f'Niestety, przegrałeś :( Gra się kończy', bg='#856ff8')
    answer.pack()

myButton = Button(root2, text="Check", fg="black", bg="grey", command=lambda: check())

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()
myButton7.pack()
myButton8.pack()

combobox.pack()

myButton.pack()

root.mainloop()
root2.mainloop()

print(client.recv(BUFFER).decode())

print(client.recv(BUFFER).decode())
