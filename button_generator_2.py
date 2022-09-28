
def button_generator(button_dic):
    for i, item in enumerate(button_dic):
        item.grid(row = (i // 4) + 1, column = i % 4)