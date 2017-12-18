#!/usr/bin/python

# A program to change the file name from American style to European style dates

import os
import shutil
import re

os.chdir('/home/xprodigy/Prog/Practice Projects/renamedates files/')

datePattern = re.compile(r'''^(.*?)
            ((0|1)?\d)-
            ((0|1|2|3)?\d)-
            ((19|20)\d\d)
            (.*?)$
            ''', re.VERBOSE)

for fileName in os.listdir():
    match = datePattern.search(fileName)
    if match:
        prefix = match.group(1)
        month = match.group(2)
        day = match.group(4)
        year = match.group(6)
        suffix = match.group(8)
        
        new_fileName = prefix + day + '-' + month + '-' + year + suffix
        print(fileName)

        #Abs pathing
        absPath = os.path.abspath('.')
        fileName = os.path.join(absPath, fileName)
        new_fileName = os.path.join(absPath, new_fileName)

        print('Renaming {o} to {n}...\n'.format(o=fileName, n=new_fileName))
        
        shutil.move(fileName, new_fileName)
        