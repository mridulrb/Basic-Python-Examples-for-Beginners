# File name: ...\\MyPythonXII\Unit1\PyChap06\countdo.py
# Program to count a word (do/Do) in a file.
import os
File1 = "Memo.TXT"
# Loop to count number the word: do or Do
def countDo():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        count = 0
        print ("The lines are ....")
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            Str = line.rstrip() # Terminates the space characters from right
            AList = Str.lower().split() # Converts into lowercase
            # Words are cheked in list
            for i in range(len(AList)):
                if AList[i] == 'do' or AList[i] == 'do.':
                    count += 1
        print ("Count of –do- in file:", count)
countDo()
