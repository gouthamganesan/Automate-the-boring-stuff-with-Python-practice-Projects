#!/usr/bin/python
# A program to generate the files required filling in gaps practice project

import os

cwd = os.getcwd()

path = os.path.join(cwd, 'files')

if not os.path.exists(path):
    os.mkdir(path)

name = input('Enter the prefix for the file names ')

while True:
    number = input('Enter the number of files to be generated ')
    if int(number) < 10000:
        break
    else:
        print('Are you trying to kill me or what?, max is 10,000')

extension = input('Enter the extension if any ')
length = len(number)
number = int(number)

for i in range(1, number + 1):
    fileName = name + str(i).rjust(length, '0') + extension
    filePath = os.path.join(path, fileName)
    if not os.path.exists(filePath):
        file = open(filePath, 'w')
        file.close()

print('Your order is delivered... ; )')
