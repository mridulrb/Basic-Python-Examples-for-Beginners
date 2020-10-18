string=raw_input("Enter string")
a,b,c,d=0,0,0,0
for s in string:
    if s.isupper():
        a=a+1
    if s.islower():
        b=b+1
    if s.isalpha():
        c=c+1
    if s.isdigit():
        d=d+1
print "Number of Capital letters",a
print "Number of Lower-case letters",b
print "Number of Alphabets letters",c
print "Number of Digits",d
