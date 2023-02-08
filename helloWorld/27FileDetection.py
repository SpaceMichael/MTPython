# coding =utf-8
# Python file detection handling tutorial example explained
import os

# path = "C:\\Users\\User\\Desktop\\test.txt"
path = "/Users//michaeltse//PycharmProjects//helloWorld//test.txt"  # for Mac

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
####
# Python reading files tutorial example explained #bro code #39
# python #read #file

try:
    with open('test.txt') as file:
        # with open('test.txt') as file: or  with open("/Users//michaeltse//PycharmProjects//helloWorld//test.txt")
        print(file.read())
        # print(file.readline())

except FileNotFoundError:
    print("That file was not found :(")

# bro code #40
text = "Yooooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt', 'a') as file:
    # file.writelines(text)
    file.write(text)
    # print(file.read())
# Python copy a file tutorial example explained bro code # 41

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)


