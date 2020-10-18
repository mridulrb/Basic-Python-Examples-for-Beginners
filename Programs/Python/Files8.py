import os
f1=open("first.txt")
t=raw_input("enter word to delete")
line=f1.readlines()
f2=open("second.txt","w")
for j in line:
    for i in j:
        if i!=t:
            f2.write(i)
f1.close()
f2.close()
f2=open("second.txt","r")
s=f2.read()
print s
