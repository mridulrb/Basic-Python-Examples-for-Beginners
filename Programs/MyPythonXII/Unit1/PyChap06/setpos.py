# File name: ...\\MyPythonXII\Unit1\PyChap06\setpos.py
import os
txtfile = "Friends.txt"
if os.path.isfile(txtfile):
    fobj = open(txtfile, 'r+')
    Friend = fobj.readline() # Function read first line
    print ("This is first line:", Friend)
    pos = fobj.tell()
    # Get the current position of the file Friends.txt.
    print ("Current position is: %d" % pos)
    fobj.seek(pos) # Goto pos byte position
    Friend = fobj.readline() # Function read current position data i.e., pos
    print ("Current position data:", Friend)
    fobj.seek(40) # Goto 40th byte position
    Friend = fobj.readline() # Reads 40th byte position data
    print ("40th position data:", Friend)    
    fobj.close()
else:
    print ("File does not exist.")
