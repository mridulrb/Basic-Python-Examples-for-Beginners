# File name: ...\\MyPythonXII\Unit1\PyChap06\copyfile.py
import os
filer = "student.txt"
filew = "stud.txt" 
if os.path.isfile(filer):
    frobj = open(filer, 'r') # File opened in read mode
    fwobj = open(filew, 'w') # File opened in write mode
    for line in frobj.readlines():
        fwobj.write(line)        
    frobj.close(), fwobj.close()
else:
    print ("File does not exist.")
