#!/usr/bin/python

import sys
import shelve
import pyperclip

mcbShelf = shelve.open('mcb')

# For two command-line arguments
if len(sys.argv) == 3:
    # To save a variable
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    # To delete a variable
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
        else:
            print('The given variable in not found...\n')

# For one command-line argument
elif len(sys.argv) == 2:
    # To delete all variables
    if sys.argv[1].lower() == 'delete':
        for item in mcbShelf.keys():
            del mcbShelf[item]

    # To copy a variable
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
    # To list all variable keys
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(list(mcbShelf.keys()))

    # To print all variables with their values
    elif sys.argv[1].lower() == 'print':
        for key, value in mcbShelf.items():
            print('\n\t' + key + ' = ' + value)

# For no command-line arguments, it prints the syntax          
elif len(sys.argv) == 1:
    print(
        '\nThe current syntax is \n\t \
        1. python mcb.pyw save <variable_name>\n\t \
        2. python mcb.pyw delete <variable_name>\n\t \
        3. python mcb.pyw delete\n\t \
        4. python mcb.pyw <variable_name>\n\t \
        5. python mcb.pyw list\n\t \
        6. python mcb.pyw print\n'
    )


mcbShelf.close()
