#!/usr/bin/python
# A program to generate gaps between file names, so that a new file can be added

import os
import shutil
import re
import sys

while True:
    pathInput = input('Enter the path of the directory (It must contain only the patterned files) ')
    if os.path.exists(pathInput):
        break
    else:
        print('Path does not exists. Try another path.')
fileNameRegex = re.compile(r'(.*?)(\d+)(\.(\w+))?')

directory = os.listdir(pathInput)
if '.directory' in directory:
    directory.remove('.directory')

nameList = []

for aFile in directory:
    if fileNameRegex.search(aFile):
        matchName = fileNameRegex.search(aFile).group(1)
        if matchName not in nameList:
            nameList += [matchName]

if len(nameList) > 1:
    print('There are more than one type of series in the directory that you gave us. Their names are, ')
    for i in nameList:
        print(i)
    while True:
        name = input('Enter the name of the series that you want to select ')
        if name in nameList:
            break
        else:
            print('Name is incorrect. Try another.')
elif len(nameList) == 0:
    print('There are no series in the directory that you have provided. \nExiting')
    sys.exit()
else:
    name = nameList[0]

number = [1000000, 0]

# To find the last number in the file series
for aFile in directory:
    if os.path.isfile(os.path.join(pathInput, aFile)) and fileNameRegex.search(aFile).group(1) == name:
        if int(fileNameRegex.search(aFile).group(2)) > number[1]:
            number[1] = int(fileNameRegex.search(aFile).group(2))
        elif int(fileNameRegex.search(aFile).group(2)) < number[0]:
            number[0] = int(fileNameRegex.search(aFile).group(2))

print('The range of the selected series is {lower} to {upper} '.format(lower=number[0], upper=number[1]))
while True:
    fileNumRemove = input('Enter the file number to remove (Or just press enter to exit)')
    if fileNumRemove == '':
        break
    if not os.path.exists(os.path.join(pathInput, 'to_delete')):
        os.mkdir(os.path.join(pathInput, 'to_delete'))
    fileNumRemove = int(fileNumRemove)
    for aFile in directory:
        if aFile.startswith(name + str(fileNumRemove).rjust(len(str(number[1])), '0')):
            if os.path.exists(os.path.join(pathInput, aFile)):
                shutil.move(os.path.join(pathInput, aFile), os.path.join(pathInput, 'to_delete', aFile))
                print('Moving {file} to {folder}'.format(file=aFile, folder='to_delete'))
            else:
                print('FileNotFound. It seems its been already removed. Try another.')

print('All done')
