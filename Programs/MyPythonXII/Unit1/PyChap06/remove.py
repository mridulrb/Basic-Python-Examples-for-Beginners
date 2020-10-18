# File name: ...\\MyPythonXII\Unit1\PyChap06\remove.py
import os
print ("Enter file name which you want to delete: ", end="")
filename = input()
if os.path.isfile(filename):
    os.remove(filename)
    print ("File successfully deleted")    
else:
    print ("File does not exist.")
