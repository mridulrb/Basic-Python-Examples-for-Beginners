# File name: ...\\MyPythonXII\Unit1\PyChap02\repch.py
# Program to replace punctuation characters with space

txt = input("Enter a string: ")
txt = txt.lower()
#replace each punctuation character with a space.
for ch in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
    txt = txt.replace(ch, ' ')
    
print ("String without punctuation characters is:", txt)
