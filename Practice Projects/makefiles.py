#!/usr/bin/python
# A program to make the files used in the program renameDates.py

import random
import string
import os


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

os.chdir('/home/xprodigy/Prog/Practice Projects/renamedates files/')

no_of_files = random.randint(10, 101)

for i in range(no_of_files):
    prefixLen = random.randint(0, 15)
    suffixLen = random.randint(0, 15)
    day = str(random.randint(1, 31))
    month = str(random.randint(1, 12))
    year = str(random.randint(19, 20)) + str(random.randint(10, 99))
    prefix = randomword(prefixLen)
    suffix = randomword(suffixLen)
    filename = '{p}{m}-{d}-{y}{s}'.format(p=prefix,
                                          m=month, d=day, y=year, s=suffix)
    file = open(filename, 'w')
    file.write(randomword(random.randint(1000, 10000)))
    file.close()
