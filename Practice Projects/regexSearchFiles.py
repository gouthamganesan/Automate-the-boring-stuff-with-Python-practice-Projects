#!/usr/bin/python

# A program to search for a user-defined regex in all the files of a folder

import os
import re

path = input('Enter the path of the folder to be searched: ')
path = os.path.abspath(path)

os.chdir(path)

files = os.listdir()

userInput = input('Enter the regex you wanna search : ')
userRegex = re.compile(r'{}'.format(userInput))

for file in files:
    if file.endswith('.txt'):
        fileObject = open(file)
        lines = fileObject.readlines()
        for line in lines:
            if userRegex.search(line):
                match = userRegex.search(line).group()
                print('Found \"{match}\" in the line {line_no} of the file {file_name}'.format(match=match, line_no=lines.index(line), file_name=file))
        fileObject.close()
