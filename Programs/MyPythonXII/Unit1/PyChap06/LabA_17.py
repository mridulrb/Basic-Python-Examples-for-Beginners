# File name: ...\\MyPythonXII\Unit1\PyChap06\vwords.py
import os
def vowelwords():
    file1 = "TEXT1.TXT"
    file2 = "TEXT2.TXT"
    if os.path.isfile(file1):
        f1 = open(file1, 'r') # File is opened in read mode
        f2 = open(file2, 'r+') # File is opened in both reading and writing mode
        VOWELS = "AEIOU" # Assign vowels to check with words
        wordcount=0 # Variable to count total words
        for lines in f1: # File object will read EOF file
            wordlist = lines.split()  # Creates a list (wordlist) using split() function
            wordcount = wordcount + len(wordlist)
        f1.seek(0) # Goto to 0th byte position
        file1data = f1.read()
        print ("TEXT1.TXT file contents:", file1data)
        print ('Number of word in TEXT1.TXT file:', str(wordcount))            
        String = ""
        for word in wordlist: # Process each word in the wordlist
            if word[0] not in VOWELS: # Check if it is not an uppercase vowel                
                String = String + word + ' ' # Add the word into a new string            
        f2.write(String) # Write into TEXT2.TXT file
        f2.seek(0) # Goto to 0th byte position
        file2data = f2.read()
        print ("TEXT2.TXT file contents:", file2data)
        f1.close()
        f2.close()
    else:
        print ("Source file does not exist.")

def main():
    vowelwords()
main()
