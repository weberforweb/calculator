
import os
os.system('cls')
import tkinter as tk
from tkinter import W
from button_generator import btn_creation

window = tk.Tk()

window.title('My Calculator')

lbl_result_screen = tk.Label(
    master = window,
    text = "Results",
    height = 5
)

button_items = [1, 2, 3,'+', 4, 5, 6, '-', 7, 8, 9,'*','.', 0, 'C', '=']

lbl_result_screen.grid(row = 0, column = 0)
btn_creation(button_items, window)


window.mainloop()