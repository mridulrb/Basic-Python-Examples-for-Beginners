# File name: ...\\MyPythonXII\Unit1\PyChap06\copyw.py
# Program to copy words starting with vowel and second character 'F'
import os
File1 = "Para.TXT"
File2 = "Vword.TXT"
# Function to copy words starting with vowel and second character 'F'
def copyWords():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        fb1 = open(File2, 'w')
        vowel = 'aeiou'
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            # Strip off the new-line character and any whitespace on the right.
            Str = line.rstrip() 
            Str = Str.lower() # Converts to lower case
            List1 = Str.split(' ') # String converted into a list with words
            listLen = len(List1) # Find the length of list
            for i in range(listLen): # Loop process all words in list
                chList = list(List1[i]) # A word converted in a character list
                if len(chList) > 1: # If list contains more than 2 character
                                    # Check for target
                    if chList[0] in vowel and chList[1] == 'f':
                        fb1.write(List1[i]+'\n')
        fb.close()
        fb1.close()
        # Open the target file see the content
    else:
        print ("Source file does not exist.")
copyWords()
