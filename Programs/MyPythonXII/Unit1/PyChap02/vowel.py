# File name: ...\\MyPythonXII\Unit1\PyChap02\vowel.py
# Program to find total number of vowels in a string
String = input("Enter a string: ")
String = String.upper()
Slen = len(String)
VOWELS = "AEIOU"
Ctr = 0
for ch in range(Slen):
    if String[ch] in VOWELS:
        Ctr += 1
if Ctr > 0:
    print("Total number of vowels are:", Ctr)
else:
    print("No vowels in string")
