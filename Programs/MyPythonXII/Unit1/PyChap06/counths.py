# File name: ...\\MyPythonXII\Unit1\PyChap06\counths.py
# Program to count a word (His/Her) in a file.
import os
File1 = "Dairy.TXT"
# Loop to count number the word: His or Her
def countHisHer():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        hiscount = hercount = 0
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            # Strip off the new-line character and any whitespace on the right.
            Str = line.rstrip() 
            AList = Str.lower().split() # Converts into lowercase
            # Words are cheked in list
            for i in range(len(AList)):
                if AList[i] == 'his' or AList[i] == 'his.':
                    hiscount += 1
                if AList[i] == 'her' or AList[i] == 'her.':
                    hercount += 1
        print()
        print ("Count Count for His:", hiscount)
        print ("Count Count for Her:", hercount)
    else:
        print ("Source file does not exist.")
        
countHisHer()
