from socket import *
from tkinter import *
from PIL import ImageTk, Image
HOST = 'localhost'
PORT = 2223

BUFFER = 1024

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST,PORT))

name = input('Podaj nazwę gracza: ').encode()

client.send(name)

root = Tk()
root.title('Guess who!?')
root.iconbitmap('Photos/zapytanie.ico')
root.geometry("542x535")
root['background'] = '#856ff8'

img_1 = ImageTk.PhotoImage(Image.open("Photos/Character_1.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("Photos/Character_2.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("Photos/Character_3.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("Photos/Character_4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("Photos/Character_5.jpg"))
img_6 = ImageTk.PhotoImage(Image.open("Photos/Character_6.jpg"))

img_7 = ImageTk.PhotoImage(Image.open("Photos/Character_7.jpg"))
img_8 = ImageTk.PhotoImage(Image.open("Photos/Character_8.jpg"))
img_9 = ImageTk.PhotoImage(Image.open("Photos/Character_9.jpg"))
img_10 = ImageTk.PhotoImage(Image.open("Photos/Character_10.jpg"))
img_11 = ImageTk.PhotoImage(Image.open("Photos/Character_11.jpg"))
img_12 = ImageTk.PhotoImage(Image.open("Photos/Character_12.jpg"))

img_13 = ImageTk.PhotoImage(Image.open("Photos/Character_13.jpg"))
img_14 = ImageTk.PhotoImage(Image.open("Photos/Character_14.jpg"))
img_15 = ImageTk.PhotoImage(Image.open("Photos/Character_15.jpg"))
img_16 = ImageTk.PhotoImage(Image.open("Photos/Character_16.jpg"))
img_17 = ImageTk.PhotoImage(Image.open("Photos/Character_17.jpg"))
img_18 = ImageTk.PhotoImage(Image.open("Photos/Character_18.jpg"))

img_19 = ImageTk.PhotoImage(Image.open("Photos/Character_19.jpg"))
img_20 = ImageTk.PhotoImage(Image.open("Photos/Character_20.jpg"))
img_21 = ImageTk.PhotoImage(Image.open("Photos/Character_21.jpg"))
img_22 = ImageTk.PhotoImage(Image.open("Photos/Character_22.jpg"))
img_23 = ImageTk.PhotoImage(Image.open("Photos/Character_23.jpg"))
img_24 = ImageTk.PhotoImage(Image.open("Photos/Character_24.jpg"))

label_1 = Label(image=img_1)
label_2 = Label(image=img_2)
label_3 = Label(image=img_3)
label_4 = Label(image=img_4)
label_5 = Label(image=img_5)
label_6 = Label(image=img_6)

label_7 = Label(image=img_7)
label_8 = Label(image=img_8)
label_9 = Label(image=img_9)
label_10 = Label(image=img_10)
label_11 = Label(image=img_11)
label_12 = Label(image=img_12)

label_13 = Label(image=img_13)
label_14 = Label(image=img_14)
label_15 = Label(image=img_15)
label_16 = Label(image=img_16)
label_17 = Label(image=img_17)
label_18 = Label(image=img_18)

label_19 = Label(image=img_19)
label_20 = Label(image=img_20)
label_21 = Label(image=img_21)
label_22 = Label(image=img_22)
label_23 = Label(image=img_23)
label_24 = Label(image=img_24)

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)
label_4.grid(row=0, column=3)
label_5.grid(row=0, column=4)
label_6.grid(row=0, column=5)

label_7.grid(row=1, column=0)
label_8.grid(row=1, column=1)
label_9.grid(row=1, column=2)
label_10.grid(row=1, column=3)
label_11.grid(row=1, column=4)
label_12.grid(row=1, column=5)

label_13.grid(row=2, column=0)
label_14.grid(row=2, column=1)
label_15.grid(row=2, column=2)
label_16.grid(row=2, column=3)
label_17.grid(row=2, column=4)
label_18.grid(row=2, column=5)

label_19.grid(row=3, column=0)
label_20.grid(row=3, column=1)
label_21.grid(row=3, column=2)
label_22.grid(row=3, column=3)
label_23.grid(row=3, column=4)
label_24.grid(row=3, column=5)

root2 = Tk()
root2.title('Guess who!?')
root2.iconbitmap('Photos/zapytanie.ico')
root2.geometry("300x400")
root2['background'] = '#856ff8'
t = client.recv(BUFFER).decode()
i = 8
txt = t + f"Punkty: {i}"
text = Label(root2, text=txt, bg='#856ff8')
text.pack()


def response1(i):
    i -= 1
    t = 'Czy_człowiek'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f' Postać przeciwnika jest człowiekiem. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie jest człowiekiem. Punkty: {i}', bg='#856ff8')
    answer.pack()

myButton1 = Button(root2, text="Czy twoja postać jest człowiekiem?", fg="black", bg="grey", command = lambda: response1(i))

def response2(i):
    i -= 1
    t = 'Czy_kobieta'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika jest kobietą. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie jest kobietą. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton2 = Button(root2, text="Czy twoja postać jest kobietą?", fg="black", bg="grey", command = lambda: response2(i))

def response3(i):
    i -= 1
    t = 'Czy_broda'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika ma brodę. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie ma brody. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton3 = Button(root2, text="Czy twoja postać ma brodę?", fg="black", bg="grey", command = lambda: response3(i))

def response4(i):
    i -= 1
    t = 'Czy_nakrycie_głowy'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika ma nakrycie głowy. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie ma nakrycia głowy. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton4 = Button(root2, text="Czy twoja postać ma nakrycie głowy?", fg="black", bg="grey", command = lambda: response4(i))

def response5(i):
    i -= 1
    t = 'Czy_złoczyńca'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika jest złoczyńcą. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie jest złoczyńcą. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton5 = Button(root2, text="Czy twoja postać jest złoczyńcą?", fg="black", bg="grey", command = lambda: response5(i))

def response6(i):
    i -= 1
    t = 'Czy_okulary'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika ma okulary. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie ma okularów. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton6 = Button(root2, text="Czy twoja postać ma okulary?", fg="black", bg="grey", command = lambda: response6(i))

def response7(i):
    i -= 1
    t = 'Czy_gruby'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika jest przy tuszy. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie jest przy tuszy. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton7 = Button(root2, text="Czy twoja postać jest przy tuszy?", fg="black", bg="grey", command = lambda: response7(i))

def response8(i):
    i -= 1
    t = 'Czy_łysy'.encode()
    client.send(t)
    x = client.recv(BUFFER).decode()
    if x == 'True':
        answer = Label(root2, text = f'Postać przeciwnika jest łysy. Punkty: {i}', bg = '#856ff8')
    else:
        answer = Label(root2, text=f'Postać przeciwnika nie jest łysy. Punkty: {i}', bg='#856ff8')
    answer.pack()
myButton8 = Button(root2, text="Czy twoja postać jest łysa?", fg="black", bg="grey", command = lambda: response8(i))

myButton = Button(root2, text="Send", fg="black", bg="grey")

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()
myButton7.pack()
myButton8.pack()

myButton.pack()

# intext = Entry(root, width=50, borderwidth=5)
# intext.grid(row=1, column=6, sticky=S)

root.mainloop()
root2.mainloop()

print(client.recv(BUFFER).decode())

print(client.recv(BUFFER).decode())