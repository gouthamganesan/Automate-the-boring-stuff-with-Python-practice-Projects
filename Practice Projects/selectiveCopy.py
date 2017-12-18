#!/usr/bin/python
# A prob to walk through the given path and filter the given extension files to a certain location

import os
import shutil

searchPath = os.path.abspath(input('The current working directory is {directory} \n Enter the location to search for...'.format(directory=os.getcwd())))
searchExtension = input('Enter the extension to search for ').lower()
destinationPath = os.path.abspath(input('Enter the path for the files to be copied...'))
for i in os.listdir(searchPath):
    if os.path.isfile(i):
        input(i)

if not os.path.exists(destinationPath):
    os.makedirs(destinationPath)

if not searchExtension.startswith('.'):
    searchExtension = '.' + searchExtension

for folder, subfolders, files in os.walk(searchPath):
    if folder == destinationPath:
        continue
    for file in files:
        if file.endswith(searchExtension):
            shutil.copy(os.path.join(folder, file), os.path.join(destinationPath, file))
            print('Copied {S} to {D}...'.format(S=os.path.join(folder, file), D=os.path.join(destinationPath, file)))
