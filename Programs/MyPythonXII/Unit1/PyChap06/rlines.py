# File name: ...\\MyPythonXII\Unit1\PyChap06\rlines.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile, 'r') # File is opened in read mode
print ("All lines from Friends.txt file")
print ("------------------------------")
while True:
    F = fobj.readline() # Function return a single line from the file
    if len(F) <= 0:
        break; # Encounter EOF
    print (F, end="")
fobj.close() # File closed to free system resources


