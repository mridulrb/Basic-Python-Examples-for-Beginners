# File name: ...\\MyPythonXII\Unit1\PyChap06\filera.py
import os
txtfile = "Friends.txt" # Text file is assigned
if os.path.isfile(txtfile):
    print ("Friends names are...")
    print ("-------------------")
    for F in open(txtfile).read(): # Both open and read the contents
        print (F, end="")        
else:
    print ("File does not exist.")
