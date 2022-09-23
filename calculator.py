
import os

from button_generator import btn_creation
os.system('cls')
import tkinter as tk
from tkinter import ttk
from button_generator import btn_creation
from show_result import insert_text

window = tk.Tk()

window.title('My Calculator')

lbl_result_screen = tk.Label(
    master = window,
    height = 3,
)

button_items = [
    {'text': '1',
    'command': lambda: insert_text('1', lbl_result_screen)},
    {'text': '2',
    'command': lambda: insert_text('2', lbl_result_screen)},
    {'text': '3',
    'command': lambda: insert_text("3", lbl_result_screen)},
    {'text': '+',
    'command': lambda: insert_text('+', lbl_result_screen)},
    {'text': '4',
    'command': lambda: insert_text('4', lbl_result_screen)},
    {'text': '5',
    'command': lambda: insert_text('5', lbl_result_screen)},
    {'text': '6',
    'command': lambda: insert_text('6', lbl_result_screen)},
    {'text': '-',
    'command': lambda: insert_text('-', lbl_result_screen)},
    {'text': '7',
    'command': lambda: insert_text('7', lbl_result_screen)},
    {'text': '8',
    'command': lambda: insert_text('8', lbl_result_screen)},
    {'text': '9',
    'command': lambda: insert_text('9', lbl_result_screen)},
    {'text': '*',
    'command': lambda: insert_text('*', lbl_result_screen)},
    {'text': '.',
    'command': lambda: insert_text('.', lbl_result_screen)},
    {'text': '0',
    'command': lambda: insert_text('0', lbl_result_screen)},
    {'text': 'C',
    'command': lambda: insert_text('C', lbl_result_screen)},
    {'text': '=',
    'command': lambda: insert_text('=', lbl_result_screen)},
]

btn_list = []
for item in button_items:
    btn_button_items = ttk.Button(
        master = window,
        text = item['text'],
        command= item['command'],
    )

    btn_list.append(btn_button_items)

lbl_result_screen.grid(row = 0, column = 0)


btn_creation(btn_list , window)

window.mainloop()