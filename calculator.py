
import os

from button_generator import btn_creation
os.system('cls')
import tkinter as tk
from tkinter import ttk
from button_generator import btn_creation

window = tk.Tk()

window.title('My Calculator')

lbl_result_screen = tk.Label(
    master = window,
    height = 3,
)
lbl_result_screen.grid(row = 0, column = 0)

def insert_text(btn_item):
    lbl_result_screen['text'] = btn_item

button_items = [
    {'text': '1',
    'command': lambda: insert_text('1')},
    {'text': '2',
    'command': lambda: insert_text('2')},
    {'text': '3',
    'command': lambda: insert_text("3")},
    {'text': '+',
    'command': lambda: insert_text('+')},
    {'text': '4',
    'command': lambda: insert_text('4')},
    {'text': '5',
    'command': lambda: insert_text('5')},
    {'text': '6',
    'command': lambda: insert_text('6')},
    {'text': '-',
    'command': lambda: insert_text('-')},
    {'text': '7',
    'command': lambda: insert_text('7')},
    {'text': '8',
    'command': lambda: insert_text('8')},
    {'text': '9',
    'command': lambda: insert_text('9')},
    {'text': '*',
    'command': lambda: insert_text('*')},
    {'text': '.',
    'command': lambda: insert_text('.')},
    {'text': '0',
    'command': lambda: insert_text('0')},
    {'text': 'C',
    'command': lambda: insert_text('C')},
    {'text': '=',
    'command': lambda: insert_text('=')},
]

btn_list = []
for item in button_items:
    btn_button_items = ttk.Button(
        master = window,
        text = item['text'],
        command= item['command'],
    )

    btn_list.append(btn_button_items)


btn_creation(btn_list , window)
window.mainloop()