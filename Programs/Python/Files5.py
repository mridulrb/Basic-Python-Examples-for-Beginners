y=open("first.txt","r")
st=y.read()
a=0
for i in st:
    if (i.isspace()):
        a=a+1
print a
y.close
