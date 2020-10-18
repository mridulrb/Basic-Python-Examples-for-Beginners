x=open("first.txt","r")
lines=x.readlines()
for line in lines:
    a=0
    for i in line:
        if(i.isspace()):
            a=a+1
    print a
x.close()

