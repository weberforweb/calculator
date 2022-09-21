
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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
math_functions = ['+', '-', '*']
last_row_items = ['.', 0, 'c', '=']


# def create_button(numbers_and_symbols):
for num in numbers:
    btn_numbers = ttk.Button(
        master = window,
        text = num,
    )    
    if num <= 3:        
        btn_numbers.grid(row = 1, column = num -1, sticky = (W,))
    elif num > 3 and num <= 6:        
        btn_numbers.grid(row = 2, column = num-4, sticky = (W,))
    else:
        btn_numbers.grid(row = 3, column = num -7, sticky = (W,))

for symbols in math_functions:
    btn_symbols = ttk.Button(
        master = window,
        text = symbols,
    )   
    btn_symbols.grid(row = (math_functions.index(symbols)+1), column = 3 )

for item in last_row_items:
    btn_last_row_items = ttk.Button(
        master = window,
        text = item
    )
    btn_last_row_items.grid(row = 4, column = last_row_items.index(item))





lbl_result_screen.grid(row = 0, column = 0)

window.mainloop()