# File name: ...\\MyPythonXII\Unit1\PyChap06\cpos.py
import os
txtfile = "Friends.txt"
if os.path.isfile(txtfile):
    fobj = open(txtfile, 'r+')
    Friend = fobj.readline() # Function read first line
    print ("This is first line:", Friend)
    pos = fobj.tell()
    # Get the current position of the file Friends.txt.
    print ("Current position is: %d" % pos)
    fobj.close()
else:
    print ("File does not exist.")
