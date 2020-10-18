x=open("first.txt","r")
lines=x.readlines()
for line in lines:
    leng=len(line)
    print leng
x.close()

