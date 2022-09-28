
import os
os.system('cls')
import tkinter as tk
from button_generator_2 import button_generator

window = tk.Tk()

button_dic = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '**', '/', 'C', '//', '%']

result_box = tk.Label(
    master = window,
    height = 3,
)

result_box.grid (row = 0, column = 0)






button_generator(button_dic)
window.mainloop()