#!/usr/bin/python
# A program to walk a path and print all the files name with size above 100MB

import os
while True:
    pathInput = os.path.abspath(input('Enter the path for the directory to search '))
    if os.path.exists(pathInput):
        break
    else:
        print('Entered path does not exists, enter a valid path ')

for folder, subFolders, files in os.walk(pathInput):
    for file in files:
        file = os.path.join(folder, file)
        if (not os.path.islink(file)) and (os.path.getsize(file) > 100000000):
            print('File {fileName} located at {path}'.format(fileName=file, path=folder))
