# File name: ...\\MyPythonXII\Unit1\PyChap06\oneline.py
import os
txtfile = "TEST.TXT" #
if os.path.isfile(txtfile):
    fb = open(txtfile, 'r') # File is opened in read mode
    while 1:
        line = fb.readline() # Read a line
        if not line:
            break	# Encounter EOF
        else:
            print (line, end="")
    fb.close()
else:
    print ("File does not exist.")

