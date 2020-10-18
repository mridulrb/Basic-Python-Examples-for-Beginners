# File name: ...\\MyPythonXII\Unit1\PyChap06\filersize.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile) # File is opened in read mode
F = fobj.read(36) # Function reads and return the 36 bytes file content
print ("Friends names are...")
print ("-------------------")
print (F)
fobj.close() # File closed to free system resources
