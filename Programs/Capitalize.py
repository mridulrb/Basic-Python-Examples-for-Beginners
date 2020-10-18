string=raw_input("enter line")
string2=""
x=len(string)
for i in range(0,x):
    a=string[i]
    if i==0:
        b=a.upper()
        string2=string2+b
    elif string[i-1].isspace():
        b=a.upper()
        string2=string2+b
    else:
            b=a.lower()
            string2=string2+b
print string2


