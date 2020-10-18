# File name: ...\\MyPythonXII\Unit1\PyChap06\rword.py
# Program to replace word in file
import os
fa = "Address.txt"
if os.path.isfile(fa):
    fobj1 = open(fa, "r") #open for read
    fobj2 = open("NAdd.txt", "w") #open for append
    for line in fobj1:
        line = line.replace("Delhi", "New Delhi")
        fobj2.write(line)
    fobj1.close()
    fobj2.close()
else:
    print ("Source file does not exist.")


