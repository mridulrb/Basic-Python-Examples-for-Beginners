# File name: ...\\MyPythonXII\Unit1\PyChap06\endwiths.py
# Program to ccount the number of  words ending with 's'
import os
File1 = "India.TXT"
if os.path.isfile(File1):
    fb = open(File1, 'r')
    print ("Words end with 's'...")
    while 1:
        line = fb.readline() # Read a line
        if not line:
            break	# Encounter EOF
        # Strip off the new-line character and any whitespace on the right.
        Str = line.rstrip()
        Str = Str.lower() 
        List1 = Str.split(' ')
        listLen = len(List1)
        for i in range(listLen): # Loop process all words in list
            chList = list(List1[i]) # A word converted in a character list
            if chList[len(chList) - 1] == 's':
                print(List1[i])
            if chList[len(chList) - 2] == 's' and chList[len(chList) - 1] == '.':
                print(List1[i])
            
    fb.close()
else:
    print ("Source file does not exist.")
