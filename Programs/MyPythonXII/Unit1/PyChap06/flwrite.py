# File name: ...\\MyPythonXII\Unit1\PyChap06\fwrite.py
# Program to enter records into Fligh.DAT
import os
File1 = "Flight.TXT"
flobj = open(File1, 'a')
if not flobj:
    print ("File does not created")
else:
    print("Enter flight information")
    ch = 'Y'
    while ch=='Y' or ch=='y':
        Fno = input("Enter flight no.: ")
        SFrom = input("Flight starting from: ")
        To = input("Flight destination: ")
        # Concatenate data to write in one line
        flobj.write(Fno.upper() + "-" + SFrom.upper() + "-" + To.upper() + "\n")
        ch = input("Add more entry? <y/n>: ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
flobj.close()
