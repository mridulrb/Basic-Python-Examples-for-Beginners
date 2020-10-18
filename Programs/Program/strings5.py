string=raw_input("Enter string")
string2=""
x=len(string)
for i in range(0,x):
    a=string[i]
    if(i%2==0):
        b=a.upper()
        string2=string2+b
    else:
        b=a.lower()
        string2=string2+b
print string2
