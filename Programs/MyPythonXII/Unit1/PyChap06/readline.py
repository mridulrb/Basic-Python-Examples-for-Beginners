# File name: ...\\MyPythonXII\Unit1\PyChap06\readline.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile, 'r') # File is opened in read mode
F = fobj.readline() # Function returns a single line from the file
print ("A line from Friends.txt file")
print ("----------------------------")
print (F)
fobj.close() # File closed to free system resources
