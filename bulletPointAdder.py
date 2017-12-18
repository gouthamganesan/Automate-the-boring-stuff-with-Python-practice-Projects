#!/usr/bin/python
# This program takes what is in the clipboard
# Converts the multi-line string to list and add * in front
# of the them all and finally converts them back to string
# Thus a bulletPointAdder program

"""Copy this before executing:
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

import pyperclip
import sys

text = pyperclip.paste()

lines = text.split('\n')

for line_number in range(len(lines)):
    lines[line_number] = '* ' + lines[line_number]

text = '\n'.join(lines)

pyperclip.copy(text)
