from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Guess who!?')
root.iconbitmap('zapytanie.ico')
root.geometry("850x540")
root['background']='#856ff8'

img_1 = ImageTk.PhotoImage(Image.open("Character_1.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("Character_2.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("Character_3.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("Character_4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("Character_5.jpg"))
img_6 = ImageTk.PhotoImage(Image.open("Character_6.jpg"))

img_7 = ImageTk.PhotoImage(Image.open("Character_7.jpg"))
img_8 = ImageTk.PhotoImage(Image.open("Character_8.jpg"))
img_9 = ImageTk.PhotoImage(Image.open("Character_9.jpg"))
img_10 = ImageTk.PhotoImage(Image.open("Character_10.jpg"))
img_11 = ImageTk.PhotoImage(Image.open("Character_11.jpg"))
img_12 = ImageTk.PhotoImage(Image.open("Character_12.jpg"))

img_13 = ImageTk.PhotoImage(Image.open("Character_13.jpg"))
img_14 = ImageTk.PhotoImage(Image.open("Character_14.jpg"))
img_15 = ImageTk.PhotoImage(Image.open("Character_15.jpg"))
img_16 = ImageTk.PhotoImage(Image.open("Character_16.jpg"))
img_17 = ImageTk.PhotoImage(Image.open("Character_17.jpg"))
img_18 = ImageTk.PhotoImage(Image.open("Character_18.jpg"))

img_19 = ImageTk.PhotoImage(Image.open("Character_19.jpg"))
img_20 = ImageTk.PhotoImage(Image.open("Character_20.jpg"))
img_21 = ImageTk.PhotoImage(Image.open("Character_21.jpg"))
img_22 = ImageTk.PhotoImage(Image.open("Character_22.jpg"))
img_23 = ImageTk.PhotoImage(Image.open("Character_23.jpg"))
img_24 = ImageTk.PhotoImage(Image.open("Character_24.jpg"))

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

text= Label(root, text="What do you wanna know?", bg='#856ff8')
text.grid(row=1, column=6, sticky=N)

intext = Entry(root, width =50, borderwidth = 5)
intext.grid(row=1, column=6, sticky=S)


myButton = Button(root, text="Send", fg="black", bg="grey")

myButton.grid(row=2, column=6, sticky=N)
root.mainloop()