#!/usr/bin/python

import re

file = open('madlibs')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter the substitute for %s: ' %j)
            text = reg.sub(inp_text, text, 1)

print(text)

file = open('madlibs_ans', 'w')
file.write(text)
file.close()
