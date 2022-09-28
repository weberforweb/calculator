
import os
os.system('cls')
import tkinter as tk
from tkinter import ttk
from button_generator_2 import button_generator

window = tk.Tk()
window.title('MY PYTHONIC CALCULATOR')

result_box = tk.Label(
    master = window,
    height = 3,
    text = '0'
)

result_box.grid (row = 0, column = 0)

BUTTON_LIST = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', 'C', '/', '**', '%', '//', '=']

def insert_item(btn_item):
    current = result_box['text']
    if btn_item == '=':
        if btn_item in BUTTON_LIST:
            result_box['text'] = str(eval(current))
    elif current == '0':
        result_box['text'] = btn_item
    elif btn_item == 'C':
        result_box['text'] = '0'
    # elif btn_item == '%':
    #     result_box['text'] = int(current)  
    else:
        result_box['text'] += btn_item

BUTTON_DIC = [
    {'text': '1',
    'command': lambda: insert_item('1')}, #if not use lambda, command run automatically
    {'text': '2',
    'command': lambda: insert_item('2')},
    {'text': '3',
    'command': lambda: insert_item('3')},
    {'text': '+',
    'command': lambda: insert_item('+')},
    {'text': '4',
    'command': lambda: insert_item('4')},
    {'text': '5',
    'command': lambda: insert_item('5')},
    {'text': '6',
    'command': lambda: insert_item('6')},
    {'text': '-',
    'command': lambda: insert_item('-')},
    {'text': '7',
    'command': lambda: insert_item('7')},
    {'text': '8',
    'command': lambda: insert_item('8')},
    {'text': '9',
    'command': lambda: insert_item('9')},
    {'text': '*',
    'command': lambda: insert_item('*')},
    {'text': '.',
    'command': lambda: insert_item('.')},
    {'text': '0',
    'command': lambda: insert_item('0')},
    {'text': 'C',
    'command': lambda: insert_item('C')},
    {'text': '/',
    'command': lambda: insert_item('/')},
    {'text': '**',
    'command': lambda: insert_item('**')},
    {'text': '%',
    'command': lambda: insert_item('%')},
    {'text': '//',
    'command': lambda: insert_item('//')},
    {'text': '=',
    'command': lambda: insert_item('=')},
]

btn_list = []
for item in BUTTON_DIC:
    button_item = ttk.Button(
            text = item['text'] ,
            command = item['command'] 
        )
    btn_list.append(button_item)


button_generator(btn_list)
window.mainloop()