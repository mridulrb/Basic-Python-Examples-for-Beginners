# File name: ...\\MyPythonXII\Unit1\PyChap06\fread.py
import os
txtfile = "E:\\MyPythonXII\\Unit1\\PyCh03\\Friends.txt"
if os.path.isfile(txtfile):
    fobj = open(txtfile) 
    print ("All line from Friends.txt file")
    print ("------------------------------")
    for F in fobj:
        print (F, end="")
    fobj.close()
else:
    print ("File does not exist.")
