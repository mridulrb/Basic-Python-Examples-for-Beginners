# File name: ...\\MyPythonXII\Unit1\PyChap06\linerda.py
import os
filename = "Student.txt" 
if os.path.isfile(filename):
    fileobj = open(filename, 'r')
    print ("Student information")
    print ("-------------------")
    for line in fileobj.readlines(): 
        print (line, end="")
    fileobj.close()
else:
    print ("File does not exist.")
