# File name: ...\\MyPythonXII\Unit1\PyChap06\rename.py
# Program to rename a file and see the contents of file
import os
fa = "NAdd.txt" # File to be renamed
if os.path.isfile(fa):
    os.rename("NAdd.txt", "MyAdd.txt")  # File renamed
    fb = "MyAdd.txt"
    obj = open(fb, "r") #open for read
    print("Content of 'MyAdd.txt' file...")
    for line in obj:
        print(line.rstrip())
    obj.close()
else:
    print ("Source file does not exist.")


