
BUTTON_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '.', '=', 'C']

def insert_text(btn_item, label):
    current = label['text']
    if btn_item == '=':
        if btn_item in BUTTON_LIST: #it is important for secure running of eval()
            label['text'] = str(eval(current)) #should convert to string for possibility of +=

    else:
        if btn_item == '+' or btn_item == '-' or btn_item == '*':
            if current[-1] == '+' or current[-1] == '-' or current[-1] == '*':
                label['text'] = current[:-1] + btn_item
            else:
                label['text'] += btn_item
        else:
            label['text'] += btn_item #with += items can concatenate