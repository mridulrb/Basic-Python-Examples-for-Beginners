# File name: ...\\MyPythonXII\Unit1\PyChap06\svowel.py
import os
def vowelwords():
    file1 = "TEXT1.TXT"
    file2 = "TEXT2.TXT"
    if os.path.isfile(txtfile):
        f1 = open(file1, 'r') # File is opened in read mode
        f2 = open(file21, 'w') # File is opened in read mode
        print("File contents are:")
        VOWELS = "AEIOU"
        Ctr = 0
        for ch in range(Slen):
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            else:
                print(line, end="")
                for i in line:
                    if i.isalpha():
                        alphabets += 1
                    if i.isdigit():
                        digits += 1
                    # if there are multiple lines,
                    # the newline (\n) will consider as one space
                    if i.isspace(): 
                        spaces += 1
        print()
        spaces = spaces - (ln - 1)
        print ("Total lines: %d" % ln)
        print ("Total alphabets are: %d" %alphabets)
        print ("Total digits are: %d" %digits)
        print ("Total spaces are: %d" %spaces)
        fb.close()
    else:
        print ("File does not exist.")
vowelwords()

