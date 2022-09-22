
from tkinter import ttk
from tkinter import W

def btn_creation(button_items , window):
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
