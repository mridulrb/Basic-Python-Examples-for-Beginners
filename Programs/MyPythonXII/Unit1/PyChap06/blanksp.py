# File name: ...\\MyPythonXII\Unit1\PyChap06\blanksp.py
# Function to count lines and blank spaces
import os
def countBlankSpaces():
    txtfile = "Notes.TXT" #
    if os.path.isfile(txtfile):
        fb = open(txtfile, 'r') # File is opened in read mode
        bspace = ln = 0
        print("File contents are:")
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            else:
                print(line, end="")
                # Strip off the new-line character and any whitespace on the right.
                line = line.rstrip()
                ln += 1 # Counts number lines read
                for i in line:
                    if i.isspace(): 
                        bspace += 1
        print()
        print ("Total lines: %d" % ln)
        print ("Total spaces are: %d" %bspace)
        fb.close()
    else:
        print ("File does not exist.")
countBlankSpaces()

