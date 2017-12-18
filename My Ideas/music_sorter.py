#!/usr/bin/python
# A program to sort the music to another fonder

import os
import shutil
import vlc

musicPath = input('Enter the path of the directory you want to search ')
copyPath = input('Enter the path of the directory you want to copy to  ')
if not os.path.exists(copyPath):
    os.mkdir(copyPath)
os.chdir(copyPath)

for folder, subfolders, files in os.walk(musicPath):
    for file in files:
        #relPath = os.path.relpath(os.path.join(folder), musicPath)
        #copyDirectory = os.path.abspath(relPath)
        #if file in os.listdir(copyDirectory):
        #    continue
        if file.endswith('.mp3'):
            print('Current folder: {} Current File: {}'.format(folder, file).ljust(150))
            song = vlc.MediaPlayer(os.path.join(folder, file))
            song.play()
            print('''Commands: 
             1. A = Advance 10% of the track 
             2. <nothing> = Next track 
             3. C = Copy to the specified folder
             ''')
            ch = input()
            while True:
                if not song.is_playing():
                    break
                if ch == '':
                    song.stop()
                    break
                elif ch == 'a':
                    song.set_position(song.get_position() + 0.1)
                elif ch == 'c':
                    relPath = os.path.relpath(os.path.join(folder), musicPath)
                    copyDirectory = os.path.abspath(relPath)
                    if not os.path.exists(copyDirectory):
                        os.mkdir(copyDirectory)
                    shutil.copy(os.path.join(folder, file), os.path.join(copyDirectory, file))
                    print('Copied {} to {}\n\n'.format(os.path.join(folder, file).rjust(50), os.path.join(copyDirectory, file).rjust(50)))
                    song.stop()
                    break
                ch = input()

'''fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                ch = ch.lower()'''