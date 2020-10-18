# File name: ...\\MyPythonXII\Unit1\PyChap06\mrgfile.py
# Program to read two files and merge data in third file.
import os
File1 = 'File1.DAT'
File2 = 'File2.DAT'
File3 = 'New.DAT'
def mergeFile(File1, File2):
    if os.path.isfile(File1) and os.path.isfile(File2):
        fobj1 = open(File1) # First source file opened in read mode
        fobj2 = open(File2) # Second source file opened in read mode
        fobj3 = open(File3, 'w')# Third file opened in append mode
        # Loop to process first file data
        while True:     # To read linewise data from data file
            f1 = fobj1.readline()
            if len(f1) <= 0:
                break; # Encounter EOF
            fobj3.write(str(f1))
        fobj1.close() # First file closed to free system resources
        # Loop to process second file data
        while True:     # To read linewise data from data file
            f2 = fobj2.readline()
            if len(f2) <= 0:
                break; # Encounter EOF
            fobj3.write(str(f2))
        fobj2.close() # second file closed to free system resources
        fobj3.close()
    else:
        print ("File does not exist")

# Calling merge function
mergeFile(File1, File2)
if os.path.isfile(File3):
    # Reading third file data
    fobj3 = open(File3, 'r') # File is opened in read mode
    print ("All line from third file")
    print ("--------------------------")
    while True:
        f3 = fobj3.readline() # Function return a single line from the file
        if len(f3) <= 0:
            break; # Encounter EOF
        print (f3, end="")
    fobj3.close() # File closed to free system resources

        
