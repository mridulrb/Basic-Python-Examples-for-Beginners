# File name: ...\\MyPythonXII\Unit1\PyChap06\capital.py
import os
File1 = "Report.TXT"
File2 = "Finerep.TXT"
# Function to capitalize sentence.
def capitalize_Sentence():
    if os.path.isfile(File1):
        fb = open(File1, 'r')
        f2 = open(File2, 'w')
        while 1:
            line = fb.readline() # Read a line
            if not line:
                break	# Encounter EOF
            # Strip off the new-line character and any whitespace on the right.
            line = line.rstrip()
            lineLength = len(line)
            String = "" # String to concatenate all character from line 
            String = String + line[0].upper()
            i = 1
            # Loop to check a line to convert uppercase
            while i < lineLength:
                if line[i] == '.':
                    String = String + line[i]
                    i += 1
                    if i >= lineLength: # If no character in line
                        break
                    if line[i] == " ":
                        String = String + line[i]
                        i += 1
                        if i >= lineLength: # If no character in line
                            break
                        String = String + line[i].upper()
                    else:
                        String = String + line[i].upper()
                else:
                    String = String + line[i]
                i += 1
            f2.write(String + '\n')
        fb.close()
        f2.close()
    else:
        print ("Source file does not exist.")

def main():
    capitalize_Sentence()
main()
