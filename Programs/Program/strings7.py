string=raw_input("Enter string")
x=0
vowel="a,e,i,o,u"
vowels=consonants=digits=special=space=0
for i in string:
    if(i in vowel):
        vowels=vowels+1
    if (i.isdigit()):
        digits=digits+1
    if((i not in vowel) and (i not in ' ') and (i.isdigit()==False)):
        consonants=consonants+1
    if(i in ' '):
        x=x+1
    if(i.isalnum()==False and i not in ' '):
        special=special+1
    if(i in ' '):
        space=space+1
    else:
        continue
print "Number of words",x+1
print "Consonant(s):",consonants-special
print "Vowel(s)",vowels
print "Digit(s):",digits
print "Alphabet(s):",consonants+vowels-special
print "Special Character(s)",special+space
