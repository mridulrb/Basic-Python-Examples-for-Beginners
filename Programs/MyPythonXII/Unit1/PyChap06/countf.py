# File name: ...\\MyPythonXII\Unit1\PyChap06\countf.py
import os
def count():
    txtfile = "STORY.TXT" #
    if os.path.isfile(txtfile):
        fb = open(txtfile, 'r') # File is opened in read mode
        alphabets = digits = spaces = ln = 0
        print("File contents are:")
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            else:
                print(line, end="")
                ln += 1 # Counts number lines read
                for i in line:
                    if i.isalpha():
                        alphabets += 1
                    if i.isdigit():
                        digits += 1
                    # if there are multiple lines,
                    # the newline (\n) will consider as one space except last line
                    if i.isspace(): 
                        spaces += 1
        print()
        print ("Total lines: %d" % ln)
        print ("Total alphabets are: %d" %alphabets)
        print ("Total digits are: %d" %digits)
        print ("Total spaces are: %d" %spaces)
        fb.close()
    else:
        print ("File does not exist.")
count()

