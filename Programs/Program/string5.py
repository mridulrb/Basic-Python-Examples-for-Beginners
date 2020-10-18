string=raw_input("Enter string")
vowel="a,e,i,o,u"
vowels=consonants=spaces=0
for i in string:
    if(i in vowel):
        vowels=vowels+1
    if i.isspace():
        spaces=spaces+1
    if(i not in vowel and i not in ' '):
        consonants=consonants+1
print "Consonant(s):",consonants
print "Vowel(s)",vowels
print "Space(s):",spaces
