# File name: ...\\MyPythonXII\Unit1\PyChap06\m5letter.py
# Program to count the number of words having length more than 5 letters
import os
File1 = "Dictionary.TXT"
if os.path.isfile(File1):
    fb = open(File1, 'r')
    print ("Words having more than 5 letters....")
    while 1:
        line = fb.readline() # Read a line
        if not line:
            break	# Encounter EOF
        # Strip off the new-line character and any whitespace on the right.
        Str = line.rstrip()
        List1 = Str.split(' ') # String converted into a list with words
        listLen = len(List1) # Find the length of list
        for i in range(listLen): # Loop process all words in list
            if len(List1[i]) > 5: # If a word more than 5 characters
                print (List1[i])
    fb.close()
else:
    print ("Source file does not exist.")
