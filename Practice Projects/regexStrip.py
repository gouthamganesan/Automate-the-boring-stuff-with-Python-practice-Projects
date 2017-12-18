
import re
import sys


def regStrip(string, char):
    regex = re.compile(r'(^[{s}]*)(.*?)([{s}]*$)'.format(s=char))
    match = regex.search(string)
    return(match.group(2))


while True:
    string_inp = input(
        'Enter the string to strip (Or just press enter to exit) ')
    if string_inp == '':
        sys.exit()
    char_inp = input(
        'Enter the char or char class to be stripped (Or just a space to strip spaces) ')
    print('The stripped output is \n' + regStrip(string_inp, char_inp))
