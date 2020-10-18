# File name: ...\\MyPythonXII\Unit1\PyChap01\uletter.py
# Counting uppercase letters using for loop
count = 0
String = "Python is a 8th Ranking Programming Language"
for letter in String:
    if letter >= "A" and letter <= "Z" :
        count += 1
print( "The string contained %d uppercase letters." % count )
