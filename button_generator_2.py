

from tkinter import ttk

# window = tk.Tk()

def button_generator(button_dic):
    for item in button_dic:
        button_item = ttk.Button(
                # master = window,
                text = item,
                # command = print('hello')
            )
        button_item.grid (row = (button_dic.index(item) // 4) + 1, column = button_dic.index(item) %4)