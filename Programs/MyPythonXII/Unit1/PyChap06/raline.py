# File name: ...\\MyPythonXII\Unit1\PyChap06\raine.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile, 'r') # File is opened in read mode
Friend = fobj.readline() # Function return the file content
print ("A line from Friends.txt file")
print ("----------------------------")
print (Friend)
fobj.close() # File closed to free system resources
