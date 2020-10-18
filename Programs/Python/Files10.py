x=open("first.txt","r")
files=x.read()
a=[]
b=[]
c=raw_input("Enter starting character")
d=0
for i in files:
    if(i.isspace()==False):
        a=a+[i]
    elif(i.isspace()):
        b=b+[''.join(a)]
        del a[0:len(a)]
print b
for j in b:
    if(j.startswith(c)):
        d=d+1
print d
