
import os
os.system('cls')
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

button_dic = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '**', '/', 'C', '//', '%']

result_box = tk.Label(
    master = window,
    height = 3,
)

result_box.grid (row = 0, column = 0)

def button_generator():
    for item in button_dic:
        button_item = ttk.Button(
                master = window,
                text = item,
                # command = print('hello')
            )
        button_item.grid (row = (button_dic.index(item) // 4) + 1, column = button_dic.index(item) %4 )




button_generator()
window.mainloop()