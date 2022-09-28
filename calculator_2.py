
import os
os.system('cls')
import tkinter as tk
from button_generator_2 import button_generator

window = tk.Tk()
window.title('MY CALCULATOR')

BUTTON_DIC = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '%', '**', '/', 'C', '//', '=']


result_box = tk.Label(
    master = window,
    height = 3,
    # text = lambda button_generator('command')
)

result_box.grid (row = 0, column = 0)



button_generator(BUTTON_DIC)
window.mainloop()