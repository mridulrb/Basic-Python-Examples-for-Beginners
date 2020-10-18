# File name: ...\\MyPythonXII\Unit1\PyChap06\filewa.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile, 'a') # File is opened in write mode
# Writting another three friends names.
fobj.write("Amit Vats\n")
fobj.write("Priyanka Dev\n")
fobj.write("Bharat Bhusan\n")
fobj.close() # File closed to free system resources
