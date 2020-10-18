string=raw_input("Enter string")
new=''
for a in string:
    if(a.isupper()==True):
        b=a.lower()
        new=new+b
    if(a.islower()==True):
        c=a.upper()
        new=new+c
    else:
        continue
print new
