# File name: ...\\MyPythonXII\Unit1\PyChap06\filerc.py
import os
txtfile = "Friend.txt" # Text file is assigned
if os.path.isfile(txtfile): # Checking the file is exist or not
    fobj = open(txtfile) # File is opened in read mode
    F = fobj.read() # Function returns entire file content to F as a string
    print ("Friends names are...")
    print ("-------------------")
    print (F)
    fobj.close() # File closed to free system resources
else:
    print ("File does not exist.")
