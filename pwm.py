#!/usr/bin/python
# CHAPTER PROJECT - 1
# An insecure password manager

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('The correct syntax is, \'pwm [account]\' to copy the account password to the clipboard ')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    print('Password for the ' + account + 'is copied to the clipboard')
    pyperclip.copy(PASSWORDS[account])
else:
    print('There is no account named, ' + account)