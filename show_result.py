
BUTTON_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '.', '=', 'C']

def insert_text(btn_item, label):
    current = label['text']
    if btn_item == 'C':
        label['text'] = '0'
    elif current == '0':
        label['text'] = btn_item
    elif btn_item == '=':
        if btn_item in BUTTON_LIST: #it is important for secure running of eval()
            label['text'] = str(eval(current)) #should convert to string for possibility of +=

    else:
        # decimal_counter = 0
        # for item in current:
        #     if item == '.':
        #         decimal_counter += 1
        if '.' in current:
            if btn_item == '.':
                # label['text'] = current.rstrip('.')
                pass
        elif btn_item in ['+', '-', '*', '.']:
            if current[-1] in ['+', '-', '*', '.']:
                label['text'] = current[:-1] + btn_item
            else:
                label['text'] += btn_item
        else:
            label['text'] += btn_item #with += items can concatenate
