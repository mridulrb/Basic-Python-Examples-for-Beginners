x=open("first.txt","r")
y=x.readlines()
z=raw_input("Enter alphabet")
a=0
for i in y:
    for j in i:
        if(j==z.upper() or j==z.lower()):
            a=a+1
print a
