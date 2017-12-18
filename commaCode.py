def comma(expression_list):
    return_str = ''
    for i in expression_list:
        if expression_list.index(i) == 0:
            return_str = i
        elif expression_list.index(i) != len(expression_list) -1:
            return_str += ', ' + i   
        else:
            return_str += ' and ' + i
            break
    return return_str

spam = ['apples', 'bananas', 'tofu', 'cats']
spam.sort()
print(comma(spam))