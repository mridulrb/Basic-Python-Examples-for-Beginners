# File name: ...\\MyPythonXII\Unit1\PyChap06\number.py
fobj = open("num.txt", 'w') # File is opened in write mode
if not fobj:
    print ("File does not created")
else:
    # Writting names into file using file object (fobj)
    for i in range(1, 11):
        fobj.write(str(i)+'\n') # File object writes only text based data.
fobj.close() # File closed to free system resources
