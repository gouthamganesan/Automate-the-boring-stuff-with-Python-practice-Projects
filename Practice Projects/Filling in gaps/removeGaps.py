#!/usr/bin/python

import os, shutil, re, sys

# Getting path from user
print('Enter the path of the directory you want to search ')
while True:
    pathInput = input()
    if os.path.exists(pathInput):
        break
    print('No can do. Path don\'t exists. Try another ')

fileNameRegex = re.compile(r'(.*?)(\d+)(\.(\w+))?')

# Removing the .directory file
directory = os.listdir(pathInput)

# Finding if there are more than one series
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

# To find the min and mac numbers in the file series
for aFile in directory:
    if os.path.isfile(os.path.join(pathInput, aFile)) and fileNameRegex.search(aFile).group(1) == name:
        if int(fileNameRegex.search(aFile).group(2)) > number[1]:
            number[1] = int(fileNameRegex.search(aFile).group(2))
        elif int(fileNameRegex.search(aFile).group(2)) < number[0]:
            number[0] = int(fileNameRegex.search(aFile).group(2))

numbers = []
# Making a list of all the numbers in the series, to find the missing numbers
selectedFileNameRegex = re.compile(r'({})(\d+)(\.(\w+))?'.format(name))
for aFile in directory:
    if selectedFileNameRegex.search(aFile):
        numbers += int(selectedFileNameRegex.search(aFile).group(2))

numbers.sort(reverse=True)

minimum, maximum = number

#for i in range(maximum, minimum - 1, -1):
 #   if i not in numbers:

