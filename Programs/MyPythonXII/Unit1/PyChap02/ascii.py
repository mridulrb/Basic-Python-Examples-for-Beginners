# File name: ...\\MyPythonXII\Unit1\PyChap02\ascii.py
# Printing ASCII code for the word 'TECHNOLOGY'
word = 'TECHNOLOGY'
wlen = len(word)
print ("Text:", end="")
for i in range(wlen):
    print("\t", word[i], end="")
print()
print("ASCII:", end="")
for i in range(wlen):
    print("\t", ord(word[i]), end="")
