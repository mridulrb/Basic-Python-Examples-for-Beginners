import os
x=open("Home.txt","r")
y=open("newfile.txt","w")
oldword=raw_input("Enter word to be replaced:")
newword=raw_input("Enter new word:")
for i in x:
    l=i.split(" ")
    for j in l:
        if(j==oldword):
            y.write(newword+" ")
        else:
            y.write(j+" ")
x.close()
y.close()
os.remove("Home.txt")
os.rename("newfile.txt","Home.txt")
