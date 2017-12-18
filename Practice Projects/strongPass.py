# A python program to check if a password is strong
# strongPass.py

import re


def checkStrength(password):
    conditions = [r'.{8,}', r'[A-Z]*', r'[a-z]*', r'[0-9]*']
    for condition in conditions:
        regex = re.compile(condition)
        match = regex.search(password)
        if not match:
            return 0
    return 1


while True:
    password_inp = input('Enter the password ( Leave blank to exit ) ')
    if not password_inp:
        break
    strength = checkStrength(password_inp)
    if strength == 1:
        print('Superb! thats a hard one to crack!')
    else:
        print('Sorry, Thats an easy one, try another combination')
