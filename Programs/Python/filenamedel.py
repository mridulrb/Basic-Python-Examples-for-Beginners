import os
f1=open("names.txt","w")
for i in range(5):
    a=raw_input("enter name:")
    f1.write(a+"\n")
f1.close()
f1=open("names.txt")
t=raw_input("enter namw to delete")
t=t+'\n'
f2=open("nnames.txt","w")
for i in f1:

    if i!=t:
        f2.write(i)
f1.close()
f2.close()
f2=open("nnames.txt","r")
s=f2.read()
print s
