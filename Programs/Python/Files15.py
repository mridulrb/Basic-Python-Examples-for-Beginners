x=open("first.txt","r")
find=raw_input("Enter word to be found")
a=0
for line in x:
    for word in line.split():
        if(word==find):
            a=a+1
print a
x.close()
