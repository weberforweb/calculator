from tkinter import Tk, Canvas, Text, Button, END

mainmenu = Tk()
mainmenu.title("PROF NAME")
mainmenu.geometry("1200x600")

canvas = Canvas(mainmenu, width=1200, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_text(600, 50, text="교수님의 초성을 입력해주세요", font="Arial 30")

letters = Text(mainmenu, width=20, height=1, font="times 15")
letters.place(x=490, y=140)


def button_click(letter):
    return lambda: letters.insert(END, letter)


btn1 = Button(mainmenu, padx=2, pady=2, text="h", font="times 12")
btn1.configure(command=button_click(btn1.cget("text")))
btn1.place(x=360, y=90)

mainmenu.mainloop()