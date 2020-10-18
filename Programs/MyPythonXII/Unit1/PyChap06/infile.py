# File name: ...\\MyPythonXII\Unit1\PyChap06\infile.py
import os
print ("Enter file name which you want to read: ", end="")
filename = input()
if os.path.isfile(filename):
    fileobj = open(filename, 'r')
    print ("File information")
    print ("----------------")
    for line in fileobj.readlines(): 
        print (line, end="")
    fileobj.close()
else:
    print ("File does not exist.")
