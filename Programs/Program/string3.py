string=raw_input("Enter string")
length=len(string)
a=0
end=length
string2=''
while a<length:
    if a==0:
        string2 +=string[0].upper()
        a += 1
    elif(string[0] =='' and string[a+1] !=''):
        string2 += string[a]
        string2 += string[a+1].upper()
        a +=2
    else:
        string2 += string[a]
        a += 1
print "Original String :",string
print "Capitalized words String:",string2
