# File name: ...\\MyPythonXII\Unit1\PyChap06\lineread.py
import os
filename = "Student.txt" 
if os.path.isfile(filename):
    fileobj = open(filename, 'r')
    Student = fileobj.readlines(1) # Reads all lines
    print ("Student information")
    print ("-------------------")
    for line in Student:
        print (line, end="")
    fileobj.close()
else:
    print ("File does not exist.")
