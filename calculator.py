
import tkinter as tk

window = tk.Tk()

window.title('My Calculator')

lbl_result_screen = tk.Label(
    master = window,
    text = "Results"
)



lbl_result_screen.grid(row = 0, column = 0)


window.mainloop()