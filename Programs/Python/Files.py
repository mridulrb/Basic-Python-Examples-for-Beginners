x=open("first.txt","r")
for line in x:
     for word in line.split():
         print line
