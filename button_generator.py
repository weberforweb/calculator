
from tkinter import W

def btn_creation(btn_list , window):
    for i , items in enumerate(btn_list): #return tuple: i=index and items=element
        if i < 4:
            items.grid(row = 1, column = i, sticky = (W,))
        elif i >= 4 and i < 8:
            items.grid(row = 2, column = i -4, sticky = (W,))
        elif i >= 8 and i < 12:
            items.grid(row = 3, column = i -8, sticky = (W,))
        else:
            items.grid(row = 4, column = i -12, sticky = (W,), pady = (0,5))
