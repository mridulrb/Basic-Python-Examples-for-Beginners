# File name: ...\\MyPythonXII\Unit1\PyChap06\filer.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile) # File is opened in read mode
F = fobj.read() # Function returns entire file content to F as a string
print ("Friends names are...")
print ("-------------------")
print (F)
fobj.close() # File closed to free system resources
