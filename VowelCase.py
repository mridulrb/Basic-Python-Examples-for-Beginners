def alphabet(x):
    v,u,l,s=0,0,0,0
    for i in x:
        if (i in "aeiou"):
            v+=1
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        if i.isspace():
            s+=1
    print ("No.of vowels is ",v)
    print ("No.of uppercase letters is ",u)
    print ("No.of lowercase letters is ",l)
    print ("No.of spaces is ",s)
x=raw_input("Enter string: ")
alphabet(x)

