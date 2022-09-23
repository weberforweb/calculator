from tkinter import *

master = Tk()

buttonClicked  = False # Bfore first click

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked 




b = Button(master, text="Smth", command=callback)
b.pack()

mainloop()