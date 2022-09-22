
import os
os.system('cls')
import tkinter as tk
from tkinter import ttk
from tkinter import W

window = tk.Tk()

window.title('My Calculator')

lbl_result_screen = tk.Label(
    master = window,
    text = "Results",
    height = 5
)

button_items = [1, 2, 3,'+', 4, 5, 6, '-', 7, 8, 9,'*','.', 0, 'C', '=']

# def create_button(button_items_and_symbols):
for items in button_items:
    btn_button_items = ttk.Button(
        master = window,
        text = items,
    )    
    if items in range(1,4) or items == '+':        
        btn_button_items.grid(row = 1, column = button_items.index(items), sticky = (W,))
    elif items in range(4,7) or items == '-':        
        btn_button_items.grid(row = 2, column = button_items.index(items) -4, sticky = (W,))
    elif items in range(7,10) or items == '*':
        btn_button_items.grid(row = 3, column = button_items.index(items) -8, sticky = (W,))
    else:
        btn_button_items.grid(row = 4, column = button_items.index(items) -12, sticky = (W,), pady = (0,5))


lbl_result_screen.grid(row = 0, column = 0)

window.mainloop()