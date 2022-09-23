
BUTTON_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '.', '=', 'C']

def insert_text(btn_item, label):
    current = label['text']
    if btn_item == '=':
        if btn_item in BUTTON_LIST: #it is important for secure running of eval()
            label['text'] = eval(current)

    else:
        label['text'] += btn_item #with += items can concatenate