

from tkinter import ttk

def button_generator(button_dic):
    for i, item in enumerate(button_dic):
        # button_item = ttk.Button(
        #         text = item,
        #         # command = print('hello')
        #     )
        item.grid(row = (i // 4) + 1, column = i % 4)