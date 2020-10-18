# File name: ...\\MyPythonXII\Unit1\PyChap06\alines.py
import os
File1 = "Lines.TXT"
# Function to count number of lines starting with 'A'
def count_A():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        ctr = 0
        print ("The lines are ....")
        while 1:
            line = fb.readline() # Read a line
            # Strip off the new-line character and any whitespace on the right.
            line = line.rstrip()
            print (line)
            if not line:
                break	# Encounter EOF
            if line[0] == 'A':
                ctr += 1
        if ctr > 0:
            print ("Total lines starting with alphabet 'A' is:", ctr)
        else:
            print ("There is no line starting with alphabet 'A'")
        fb.close()
    else:
        print ("Source file does not exist.")
def main():
    count_A()
main()
