# coding =utf-8
# copyfile() =  copies contents of a file
# copy() =       copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil
import os

# shutil.copyfile('test.txt', 'copy.txt')  # src,dst
# source = "C:\\Users\\User\\Desktop\\source.txt"
source = "test.txt"
# destination = "C:\\Users\\User\\Desktop\\destina.txt"
destination = "testmove.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
