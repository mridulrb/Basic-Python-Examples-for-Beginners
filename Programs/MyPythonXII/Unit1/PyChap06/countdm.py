# File name: ...\\MyPythonXII\Unit1\PyChap06\countdm.py
import os
File1 = "Delhi.TXT"
# Function to count number of lines starting with 'D' or 'M'
def countDM():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        ctr = 0
        print ("The lines are ....")
        while 1:
            Line = fb.readline() # Read a line
            # Strip off the new-line character and any whitespace on the right.
            Line = Line.rstrip()
            print (Line)
            if not Line:
                break	# Encounter EOF
            if Line[0] == 'D' or Line[0] == 'M':
                ctr += 1
        if ctr > 0:
            print ("Total lines starting with alphabet 'D' or 'M' is:", ctr)
        else:
            print ("There is no line starting with alphabet 'D' or 'M'")
        fb.close()
    else:
        print ("Source file does not exist.")
def main():
    countDM()
main()
