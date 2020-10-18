# File name: ...\\MyPythonXII\Unit1\PyChap06\filew.py
txtfile = "Friends.txt" # Text file is assigned
fobj = open(txtfile, 'w') # File is opened in write mode
if not fobj:
    print ("File does not created")
else:
    # Writting names into file using file object (fobj)
    fobj.write("Sanjay Mehra\n")
    fobj.write("Vinod Kapoor\n")
    fobj.write("Ravi Mehta\n")
    fobj.write("Rajat Sharma\n")
    fobj.write("Monika Ghai\n")
fobj.close() # File closed to free system resources
